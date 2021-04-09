import requests
import os 
    
class apiClient:
    def __init__(self, url_base, username, password, token='', ssl_verify=True):
        self.url_base = url_base
        self.username = username
        self.password = password
        self.token = token
        self.ssl_verify = ssl_verify
        self.response = requests.Response() 

    def __str__(self):
        result = '{'
        result += '\turl_base: '+self.url_base
        result += '\tusername: '+self.username
        result += '\tpassword: '+self.password
        result += '\ttoken: '+self.token
        result += '\tssl_verify: '+str(self.ssl_verify)
        result += '\tresponse: '+self.response.text
        result += '}'
        return result 


    def send_request(self, url_suffix, method, head, data):
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']
        switcher ={
                "GET": requests.get(self.url_base + url_suffix, headers = head,
                                    verify = self.ssl_verify),
                
                "POST": requests.post(self.url_base + url_suffix, headers = head,
                                    json = data, verify = self.ssl_verify),
                
                "PUT": requests.put(self.url_base + url_suffix, headers = head,
                                    json = data, verify = self.ssl_verify),
                
                "DELETE":requests.delete(self.url_base + url_suffix, headers = head,
                                    verify=self.ssl_verify),
                }
        self.response = switcher[method]

    def handle_response(self):
        switcher ={
                "200" :"",
                "201" :"",
                "401" :"",
                "403" :"",
                "404" :"",
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

