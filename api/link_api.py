import requests
import os 
import json
from api.api import apiException 
    
url = str(os.environ.get('API_SERVER_URL'))+'topology/link'

class linkApi:
    def post_link(link, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        data = {
                "name": link.cf.name,
                "label": link.cf.label,
                "description": link.cf.description,
                "info": link.cf.info,
                "srcVltpId": link.src_ltp.cf.cf_id,
                "destVltpId": link.dest_ltp.cf.cf_id
             }
        response = requests.post(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        if not 200 <= response.status_code <=399:
            print(response.text)
            raise apiException(status=response.status_code, reason=response.reason)
            return
        return str.split(response.headers['Location'],'/')[2]

    def get_link(link_id, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(link_id)
        response = requests.get(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        print(response.status)
        return response.body

    def get_links(auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        response = requests.get(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.body

    def del_link(link_id, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/" + link_id
        response = requests.get(
                    url,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
	
    def put_link(link, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        url += "/"+str(link.cf.cf_id)
        data = {
                "name": link.cf.name,
                "label": link.cf.label,
                "description": link.cf.description,
                "info": link.cf.info,
                "srcVltpId": 0,
                "destVltpId": 1
             }
        response = requests.post(
                    url,
                    json = json.dumps(data),
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )

