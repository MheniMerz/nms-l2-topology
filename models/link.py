'''
Link object Description:
    {
      common_fields {
        "id": 0,
        "name": "string",
        "label": "string",
        "description": "string",
        "info": {},
      }
      "srcVltpId": 0,
      "destVltpId": 0
    }
'''
from models.common_fields import CommonFields

class Link:
    def __init__(self, src_ltp: "Ltp", dest_ltp: "Ltp"):
        name = "<-->".join([src_ltp.cf.name, dest_ltp.cf.name])
        self.cf = CommonFields(name, name)
        self.src_ltp = src_ltp
        self.dest_ltp = dest_ltp

    def to_string(self) -> str:
        result = "{\n\t"
        result += self.cf.to_string()
        result += "src_ltp: "+self.src_ltp+"\n\t"
        result += "dest_ltp: "+self.dest_ltp+"\n\t"
        result += "}\n\t"
        return result
