'''
Node Object Description:
    {
     common_fields{
      "id": 0,
      "name": "string",
      "label": "string",
      "description": "string",
      "info": {}
     }
     "vsubnetId": 0,
     "hwaddr": "string",
     "status": "UP",
     "type": "switch",
     "posx": 0,
     "posy": 0,
     "location": "string"
    }
'''
import json
from models.common_fields import CommonFields

class Node:
    def __init__(self, name: str, label:str, hwaddr: str, location:str,  mgmt_ip: str, capability: str, status="UP", subnet_id=0, description=""):
        self.cf = CommonFields(name,label,0,description)
        self.hwaddr = hwaddr
        self.location = location
        self.mgmt_ip = mgmt_ip
        self.node_type = self.lldp_capability_to_device_type(capability)
        self.status = status
        self.subnet_id=subnet_id
        self.ltps: dict [str, "Ltp"] = {}

    def to_string(self) -> str:
        result  = "{\n\t"
        result += self.cf.to_string()
        result += "subnet: "+self.subnet +"\n\t"
        result += "hwaddr: "+self.hwaddr +"\n\t"
        result += "status: "+self.status +"\n\t"
        result += "device_type: "+ self.node_type +"\n\t"
        result += "location: "+self.location +"\n\t"
        result += "management_ip: "+self.mgmt_ip +"\n\t"
        result += "ltps: [\n\t"+self.ltps_to_string()+"]"
        result += "\n}"
        return result

    def add_ltp(self, ltp: "Ltp") -> None:
        self.ltps[ltp.cf.name] = ltp
    
    def ltps_to_string(self) -> str:
        result = ""
        for k in self.ltps:
            result += self.ltps[k].to_string()
        return result

    def is_switch(self) -> bool:
        if self.node_type == "Switch":
            return True
        return False
    
    def is_router(self) -> bool:
        if self.node_type == "Router":
            return True
        return False

    def name_from_fqdn(self) -> str:
        return self.cf.name.split(".")[0]

    @staticmethod
    def lldp_capability_to_device_type(cap: str) -> str:
        result = "Unkown"
        switcher = {
                "R":"Router",
                "B":"Bridge",
                "T":"Telephone",
                "C":"DOCSIS Cable Device",
                "W":"WLAN Access Point",
                "P":"Repeater",
                "S":"Station",
                "O":"Other",
                "" :"Switch"
                }
        result  = switcher[cap]
        return result


