import requests

    
auth_token='mheni'
head = {'Authorization': 'Bearer ' + auth_token}
url = 'http://172.17.0.3:8080/api/topology/link'
class linkApi:
    def post_link(link):
        data = {
                "name": link.cf.name,
                "label": link.cf.label,
                "description": link.cf.description,
                "info": link.cf.info,
                "srcVltpId": 0,
                "destVltpId": 1
             }
        response = requests.post(url, json=data, headers=head)
        print(response.json())
