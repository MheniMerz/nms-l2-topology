'''
subnet object Description:
    {
      common_fields {
        "id": 0,
        "name": "string",
        "label": "string",
        "description": "string",
        "info": {},
      }
    }
'''
from models.common_fields import CommonFields

class Subnet:
    def __init__(self, name):
        self.cf = CommonFields(name, name)

    def to_string(self) -> str:
        result = "{\n\t"
        result += self.cf.to_string()
        result += "}\n\t"
        return result
