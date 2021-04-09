import requests
import os
import json
import logging 
from api.api import apiException

class ctpApi:
    def post_ctp(ctp, api_client):
        head = {'Authorization': 'Bearer ' + api_client.token}
        data = {
                "name": ctp.cf.name,
                "label": ctp.cf.label,
                "description": ctp.cf.description,
                "info": ctp.cf.info,
                "parentId": ctp.parentId,
                "connType": ctp.connType,
                "connInfo": ctp.connInfo,
                "status": ctp.status
             }
        #print('post_api: '+str(data))
        api_client.send_request(url_suffix='topology/ctp', method='POST',
                                head=head, data=data)
        if api_client.response.status_code == 201:
            logging.info(str(api_client.response.status_code)+' CTP created successfully')
            print(str(api_client.response.status_code)+' CTP created successfully')
            return str.split(api_client.response.headers['Location'],'/')[2]
        #logging.warning(str(api_client.response.status_code)+' failed to create CTP')
        return

