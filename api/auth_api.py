import requests
import os 

url = str(os.environ.get('API_SERVER_URL'))+'login/user'
head = {'accept': 'application/json', 'Content-Type': 'application/json'}
class authApi:
    def login(auth):
        data = {
                "username": auth.username,
                "password": auth.password
             }
        response = requests.post(
                    url,
                    json = data, 
                    headers = head,
                    verify = os.environ.get('CERT_VERIFY')=='True'
                    )
        return response.text
