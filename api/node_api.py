import requests
import os 
import json 
import logging 
from api.api import apiException
    
auth_token= str(os.environ.get('API_AUTH_TOKEN'))
url = str(os.environ.get('API_SERVER_URL'))+'topology/node'

class nodeApi:
    def post_node(node, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        data = {
                "name": node.cf.name,
                "label": node.cf.label,
                "description": node.cf.description,
                "info": node.cf.info,
                "vsubnetId": node.subnet_id,
                "hwaddr": node.hwaddr,
                "status": node.status,
                "type": node.node_type,
                "posx": 200,
                "posy": 200,
                "location": node.location
             }
        response = requests.post(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify=os.environ.get('CERT_VERIFY')=='True'
                    )
        #if not 200 <= response.status_code <=399:
        #    raise apiException(status=response.status_code, reason=response.reason)
        if response.status_code == 201:
            logging.info(str(response.status_code)+' NODE created successfully')
            return str.split(response.headers['Location'],'/')[2]
        logging.warning(str(response.status_code)+' failed to create NODE')
        return
    
    def get_node(node_id, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(node_id)
        response = requests.post(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.body

    def get_nodes(auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        response = requests.post(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.body

    def del_node(node_id, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(node_id)
        response = requests.delete(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )

    def put_node(node, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(node.cf.cf_id)
        data = {
                "name": node.cf.name,
                "label": node.cf.label,
                "description": node.cf.description,
                "info": node.cf.info,
                "vsubnetId": node.subnet_id,
                "hwaddr": node.hwaddr,
                "status": node.status,
                "type": node.node_type,
                "posx": 200,
                "posy": 200,
                "location": node.location
             }
        response = requests.put(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )

