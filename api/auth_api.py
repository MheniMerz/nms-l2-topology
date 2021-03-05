import requests
import os 

class authApi:

    def login(api_client):
        head = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {
                "username": api_client.username,
                "password": api_client.password
             }
        api_client.send_request(url_suffix='login/user', method='POST',
                                head=head, data=data)
        api_client.token = api_client.response.text
