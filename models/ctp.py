'''
Ctp object:
    {
      common_fields {
        "id": 0,
        "name": "string",
        "label": "string",
        "description": "string",
        "info": {},
      }
      "parentId": 0,
      "connType": "Ether",
      "connInfo": {
        "address": "string",
        "vlan": {
          "vlanId": 0,
          "isNative": true
        }
      }
    }
'''
import json
from models.common_fields import CommonFields 

class Ctp:
    def __init__(self, name, mac, p_status, ip, vlan_id, ltp_id, node_id):
        self.cf = CommonFields(name, name)
        self.mac_address = mac
        self.status = p_status
        self.ip_address = ip
        self.vlan_id = vlan_id
        self.ltp_id = ltp_id
        self.node_id = node_id

    def to_string(self) -> str:
        result = "{\n\t\t"
        result += self.cf.to_string()
        result += "ip_address: "+self.ip_address+"\n\t\t"
        result += "mac_address: "+self.mac_address+"\n\t\t"
        result += "status: "+self.status+"\n\t\t"
        result += "access_vlan: "+self.vlan_id+"\n\t\t"
        result += "}\n\t\t"
        return result

    def assign_access_vlan(self, vlan:str):
        self.vlan_id = vlan
