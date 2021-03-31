import os
import time 
import logging
import netmiko
import configparser
import json
import concurrent.futures
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from types import SimpleNamespace
from ntc_templates.parse import parse_output
from api.node_api import nodeApi
from api.ltp_api import ltpApi
from api.link_api import linkApi
from api.ctp_api import ctpApi
from api.subnet_api import subnetApi
from api.auth_api import authApi
from api.api import apiClient
from models.node import Node
from models.ltp import Ltp
from models.ctp import Ctp
from models.link import Link
from models.auth import Auth
from models.subnet import Subnet

def run_cmd(ip, dev_type, username, password, command):
    try:
        # create connection
        connection = netmiko.ConnectHandler(
                ip=ip,
                device_type=dev_type,
                username=username,
                password=password,
        )
        # run the first command to get the ltps on the current node
        result = connection.send_command(command)
    except (AuthenticationException):
        print("***** AUTHENTICATION ERROR when connecting to "+ip+" *****")
        return
    except (SSHException):
        print("***** SSH ERROR when connecting to "+ip+" *****")
        return
    except (NetMikoTimeoutException):
        print("***** TIMEOUT ERROR when connecting to "+ip+" *****") 
        return
    except :
        print("***** UNKONWN ERROR when connecting to "+ip+" *****")
        return
    # use ntc_templates to parse the output into json
    parsed_result = parse_output(
            platform = dev_type,
            command = command,
            data = result
            )
    # beutify the json file 
    parsed_result = json.dumps(parsed_result, indent=2)
    connection.disconnect()
    return parsed_result 


def get_nodes():
    return_value = ""
    threads = list()
    for device in json.loads(config['TARGETS']['devices']):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(
                    run_cmd,
                    device,
                    "cisco_ios",
                    config['AUTH']['username'],
                    config['AUTH']['password'],
                    "show lldp neighbors detail"
            )
            return_value = future.result()
            neighbors = json.loads(return_value, object_hook=lambda d: SimpleNamespace(**d))
        for i in neighbors:
            #print(i)
            nb = i.neighbor.split(".")[0].lower() 
            if nb not in nodes:
                nodes[nb] = Node(
                        i.neighbor,
                        i.neighbor,
                        i.chassis_id,
                        "NIST B222/B215, Gaithersubrg MD",
                        i.management_ip, 
                        i.capabilities,
                        subnetObj.cf.cf_id)
            if i.local_interface != "" and i.neighbor_interface != "":
                key = device.upper()+"."+Ltp.normalize_ltp(i.local_interface)
                key +="<->"
                key += nb.upper()+"."+Ltp.normalize_ltp(i.neighbor_interface)
                links[key]= Link(i.local_interface,i.neighbor_interface)                

def get_ltps():
    threads = list()
    for device in json.loads(config['TARGETS']['devices']):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(
                    run_cmd,
                    device,
                    "cisco_ios",
                    config['AUTH']['username'],
                    config['AUTH']['password'],
                    "show interface"
                    )
            return_value = future.result()
        ints = json.loads(return_value, object_hook=lambda d: SimpleNamespace(**d))
        for i in ints:
            if str.split(i.interface,".")[0] not in nodes[device].ltps:
                nodes[device].add_ltp(Ltp(
                i.interface,
                i.link_status,
                i.bandwidth,
                i.mtu,
                nodes[device].cf.cf_id,
                i.address,
                i.description
                ))
                nodes[device].ltps[str.split(i.interface,".")[0]].add_ctp(Ctp(
                    i.interface,
                    nodes[device].ltps[str.split(i.interface,".")[0]].cf.cf_id,
                    i.encapsulation,
                    i.address,
                    i.protocol_status,
                    1,
                    1,
                    i.ip_address
                ))
        set_vlan_for_ltp(nodes[device])

def set_vlan_for_ltp(device):
    if device.is_switch():
        dev_name = device.name_from_fqdn()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(
                    run_cmd,
                    dev_name,
                    "cisco_ios",
                    config['AUTH']['username'],
                    config['AUTH']['password'],
                    "show interfaces switchport"
                    )
            return_value = future.result()
            ports= json.loads(return_value, object_hook=lambda d: SimpleNamespace(**d))
            for p in ports:
                tmp = Ltp.normalize_ltp(p.interface)
                nodes[dev_name].ltps[str.split(tmp,".")[0]].ctps[tmp].assign_access_vlan(p.access_vlan)
                nodes[dev_name].ltps[tmp].assign_native_vlan(p.native_vlan)

if __name__ == '__main__':
    #set env variables
    repeat_timer = os.environ.get('REPEAT_TIMER') 
    conf_file = os.environ.get('CONF_FILE')
    url_base = os.environ.get('API_SERVER_URL')
    ssl_verify = os.environ.get('CERT_VERIFY')=='True'
    #create logger
    log = logging.getLogger()
    # make it print to the console.
    console = logging.StreamHandler()
    log.addHandler(console)
    
    # open config file
    try:
        config = configparser.ConfigParser()
        config.read(conf_file)
        config.sections()
    except IOError:
        log.critical("*********** ERROR reading config file **********")
        exit(1)
    
    # global variables that hold the results
    nodes = {}
    links = {}
    
    # check config file for mandatory sections
    if 'TARGETS' not in config or 'AUTH' not in config:
        log.critical('Syntax error in configuration file. Please provide AUTH and TARGETS')
        log.critical('ERROR: failed to load the configuration file')
        log.critical('Exiting')
        exit(1)
    
    
    api_client = apiClient(url_base, username='admin', password='admin',
                            token='', ssl_verify=ssl_verify)
    authApi.login(api_client)
    print('AUTH_TOKEN: '+api_client.token)
    subnetObj = Subnet("test_subnet")
    subnetObj.cf.cf_id = subnetApi.post_subnet(subnetObj, api_client)
    if(repeat_timer == None):
        get_nodes()
        get_ltps()
        for n in nodes:
            nodeApi.post_node(nodes[n],api_client)
            for i in nodes[n].ltps.values():
                ltpApi.post_ltp(i, api_client)
    else:
        while(True):
            get_nodes()
            for n in nodes:
                nodes[n].cf.cf_id = nodeApi.post_node(nodes[n], api_client)
            get_ltps()
            for n in nodes:
                for l in nodes[n].ltps.values():
                    l.cf.cf_id = ltpApi.post_ltp(l, api_client)
                    for k in links.keys():
                        link_src = nodes[n].cf.name.split(".")[0].upper()
                        link_src += "."+str(l.cf.name)+"<"
                        link_dest = ">"+nodes[n].cf.name.split(".")[0].upper()
                        link_dest += "."+str(l.cf.name) 
                        if link_src in str(k):
                            links[k].src_ltp_id = l.cf.cf_id
                        if link_dest in k:
                            links[k].dest_ltp_id = l.cf.cf_id
            for n in nodes:
                for l in nodes[n].ltps.values():
                    for c in l.ctps.values():
                        c.parentId = l.cf.cf_id
                        c.cf.cf_id = ctpApi.post_ctp(c, api_client)
            for l in links.values():
                l.cf.cf_id = linkApi.post_link(l, api_client)
            time.sleep(int(repeat_timer))
    
