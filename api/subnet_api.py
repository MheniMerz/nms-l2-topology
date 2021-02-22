import requests
import os 
import json 
import logging
from api.api import apiException

auth_token= str(os.environ.get('API_AUTH_TOKEN'))
url = str(os.environ.get('API_SERVER_URL'))+'topology/subnet'

class subnetApi:
    def post_subnet(subnet, auth):
        head = {'accept':'*/*', 'Authorization': 'Bearer ' + auth.token}
        data = {
                "name": subnet.cf.name,
                "label": subnet.cf.label,
                "description": subnet.cf.description,
                "info": subnet.cf.info,
             }
        response = requests.post(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        if response.status_code == 201:
            logging.info(str(response.status_code)+' SUBNET created successfully')
            return str.split(response.headers['Location'],'/')[2]
        #if not 200 <= response.status_code <= 299:
        #    raise apiException(status=response.status_code, reason=response.reason)
        logging.warning(str(response.status_code)+' failed to create SUBNET')
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
        
    
