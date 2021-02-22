from .models.auth import Auth
from .api.auth import authApi

authObj = Auth()
authApi.login(authObj)

print(authObj.token)
