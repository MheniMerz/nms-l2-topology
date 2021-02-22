import requests
import os 
    
class apiClient:
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth
        self.response = ""

    def send_request(self, method):
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 
                            'PUT', 'PATCH', 'OPTIONS']
        

    def handle_response(self):
        switcher ={
                "200" :"" ,
                "201" :"" ,
                "401" :"" ,
                "403" :"" ,
                "404" :"" ,
                "500" :"" 
                }

class apiException(Exception):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

