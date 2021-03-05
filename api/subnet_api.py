import requests
import os 
import json 
import logging
from api.api import apiException


class subnetApi:
    def post_subnet(subnet, api_client):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + api_client.token}
        data = {
                "name": subnet.cf.name,
                "label": subnet.cf.label,
                "description": subnet.cf.description,
                "info": subnet.cf.info,
             }
        api_client.send_request(url_suffix='topology/subnet', method='POST',
                                head=head, data=data)
        
        if api_client.response.status_code == 201:
            logging.info(str(api_client.response.status_code)+' SUBNET created successfully')
            print(str(api_client.response.status_code)+' SUBNET created successfully')
            return str.split(api_client.response.headers['Location'],'/')[2]
        logging.warning(str(api_client.response.status_code)+' failed to create SUBNET')
        return
    
    def get_subnet(subnet_id, auth):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(subnet_id)
        response = requests.get(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.body
    
    def get_subnets(auth):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + auth.token}
        response = requests.get(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.body

    def del_subnet(subnet_id, auth):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(subnet_id)
        response = requests.delete(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='Ture'
                    )
    
    def put_subnet(subnet, auth):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(subnet.cf.cf_id)
        data = {
                "name": subnet.cf.name,
                "label": subnet.cf.label,
                "description": subnet.cf.description,
                "info": subnet.cf.info
             }
        response = requests.put(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        
    
