import requests

    
auth_token='mheni'
head = {'Authorization': 'Bearer ' + auth_token}
url = 'http://172.17.0.3:8080/api/topology/ltp'
class ltpApi:
    def post_ltp(ltp):
        data = {
                "name": ltp.cf.name,
                "label": ltp.cf.label,
                "description": ltp.cf.description,
                "info": ltp.cf.info,
                "vnodeId": 0, 
                "busy": True,
                "port": ltp.port
             }
        response = requests.post(url, json=data, headers=head)
        print(response.json())
