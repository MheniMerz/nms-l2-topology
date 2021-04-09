'''
Auth object Description:
    {
      "username": "admin",
      "password": "admin",
      "token": "string"
    }
'''

class Auth:
    def __init__(self, username="admin", password="admin", token=""):
        self.username=username
        self.password=password
        self.token=token
