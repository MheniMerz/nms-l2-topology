'''
Lc object Description:
    {
      common_fields {
        "id": 0,
        "name": "string",
        "label": "string",
        "description": "string",
        "info": {},
      }
      "vlinkId": 0,
      "srcVctpId": 0,
      "destVctpId": 0
    }
'''
from models.common_fields import CommonFields

class Lc:
    def __init__(self, src_ctp: "Ctp", dest_ctp: "Ctp"):
        name = "<-->".join([src_ctp.cf.name, dest_ctp.cf.name])
        self.cf = CommonFields(name, name)
        self.src_ctp = src_ctp
        self.dest_ctp = dest_ctp

    def to_string(self) -> str:
        result = "{\n\t"
        result += self.cf.to_string()
        result += "src_ctp: "+self.src_ctp+"\n\t"
        result += "dest_ctp: "+self.dest_ctp+"\n\t"
        result += "}\n\t"
        return result
