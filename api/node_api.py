import requests
import os 
import json 
import logging 
from api.api import apiException
    
class nodeApi:
    def post_node(node, api_client):
        head = {'Authorization': 'Bearer ' + api_client.token}
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
        api_client.send_request(url_suffix='topology/node', method='POST',
                                head=head, data=data)
        if api_client.response.status_code == 201:
            print(str(api_client.response.status_code)+' NODE created successfully')
            logging.info(str(api_client.response.status_code)+' NODE created successfully')
            return str.split(api_client.response.headers['Location'],'/')[2]
        logging.warning(str(api_client.response.status_code)+' failed to create NODE')
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

