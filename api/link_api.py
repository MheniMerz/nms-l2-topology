import requests
import os 
import json
import logging 
from api.api import apiException 
    
class linkApi:
    def post_link(link, api_client):
        head = {'Authorization': 'Bearer ' + api_client.token}
        data = {
                "name": link.cf.name,
                "label": link.cf.label,
                "description": link.cf.description,
                "info": link.cf.info,
                "srcVltpId": link.src_ltp_id,
                "destVltpId": link.dest_ltp_id,
                "status": link.status
             }
        print('post_api: '+str(data))
        api_client.send_request(url_suffix='topology/link', method='POST',
                                head=head, data=data)
        if api_client.response.status_code ==201:
            logging.info(str(api_client.response.status_code)+' LINK created successfully')
            print(str(api_client.response.status_code)+' LINK created successfully')
            return str.split(api_client.response.headers['Location'],'/')[2]
        logging.warning(str(api_client.response.status_code)+' failed to create LINK')
        return

