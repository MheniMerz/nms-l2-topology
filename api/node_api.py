import requests

    
auth_token='mheni'
head = {'Authorization': 'Bearer ' + auth_token}
url = 'http://172.17.0.3:8080/api/topology/node'
class nodeApi:
    def post_node(node):
        data = {
                "name": node.cf.name,
                "label": node.cf.label,
                "description": node.cf.description,
                "info": node.cf.info,
                "vsubnetId": node.subnet_id,
                "hwaddr": node.hwaddr,
                "status": node.status,
                "type": node.node_type,
                "posx": 0,
                "posy": 0,
                "location": node.location
             }
        response = requests.post(url, json=data, headers=head)
        print(response.json())
