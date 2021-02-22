import requests
import os 
import json
import logging 
from api.api import apiException
    
url = str(os.environ.get('API_SERVER_URL'))+'topology/ltp'

class ltpApi:
    def post_ltp(ltp, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
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
        response = requests.post(
                    url,
                    json = data,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        #if not 200<= response.status_code <= 299 :
        #    raise apiException(status=response.status_code, reason=response.reason)
        if response.status_code ==201:
            logging.info(str(response.status_code)+' LTP created successfully')
            return str.split(response.headers['Location'],'/')[2]
        logging.warning(str(response.status_code)+' failed to create LTP')
        return
