import netmiko
import json
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from ntc_templates.parse import parse_output

class sendQuery:
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

