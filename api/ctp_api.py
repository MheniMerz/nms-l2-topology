import requests

    
auth_token='mheni'
head = {'Authorization': 'Bearer ' + auth_token}
url = 'http://172.17.0.3:8080/api/topology/ctp'
class ctpApi:
    def post_ctp(ctp):
        data = {
                "name": ctp.cf.name,
                "label": ctp.cf.label,
                "description": ctp.cf.description,
                "info": ctp.cf.info,
                "vlinkId": 1,
                "vltpId": 1
             }
        response = requests.post(url, json=data, headers=head)
        print(response.json())
