import requests
import os 
import json
import logging 
from api.api import apiException
    
class ltpApi:
    def post_ltp(ltp, api_client):
        head = {'Authorization': 'Bearer ' + api_client.token}
        data = {
                "name": ltp.cf.name,
                "label": ltp.cf.label,
                "description": ltp.cf.description,
                "info": ltp.cf.info,
                "vnodeId": ltp.node_id, 
                "port": ltp.port,
                "bandwidth": ltp.bandwidth,
                "mtu": ltp.mtu,
                "status": ltp.status
             }
        api_client.send_request(url_suffix='topology/ltp', method='POST',
                                head=head, data=data)
        if api_client.response.status_code ==201:
            #print(str(api_client.response.status_code)+' LTP created successfully')
            logging.info(str(api_client.response.status_code)+' LTP created successfully')
            return str.split(api_client.response.headers['Location'],'/')[2]
        logging.warning(str(api_client.response.status_code)+' failed to create LTP')
        return
