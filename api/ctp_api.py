import requests
import os
import json
from api.api import apiException

url = str(os.environ.get('API_SERVER_URL'))+"topology/ctp"
class ctpApi:
    def post_ctp(ctp, auth):
        head = {'Authorization': 'Bearer ' + auth.token}
        data = {
                "name": ctp.cf.name,
                "label": ctp.cf.label,
                "description": ctp.cf.description,
                "info": ctp.cf.info,
                "parentId": ctp.parentId,
                "connType": ctp.connType,
                "connInfo": ctp.connInfo
             }
        response = requests.post(
                    url, 
                    json = data,
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        if not 200<= response.status_code <= 299 : 
            raise apiException(status=response.status_code, reason=response.reason)
            return
        return str.split(response.headers['Location'],'/')[2]
