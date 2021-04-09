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
    def __init__(self, src_ltp_name, dest_ltp_name, dest_ltp_id = 0, src_ltp_id = 0, status="UP"):
        name = "<-->".join([src_ltp_name, dest_ltp_name])
        self.cf = CommonFields(name, name)
        self.src_ltp_name = src_ltp_name
        self.dest_ltp_name = dest_ltp_name
        self.src_ltp_id = src_ltp_id
        self.dest_ltp_id = dest_ltp_id
        self.status = status

    def to_string(self) -> str:
        result = "{\n\t"
        result += self.cf.to_string()
        result += "src_ltp: "+self.src_ltp_name+"\n\t"
        result += "dest_ltp: "+self.dest_ltp_name+"\n\t"
        result += "}\n\t"
        return result
