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
      "status": "string"
    }
'''
import json
from models.common_fields import CommonFields 

class Ctp:
    def __init__(self, name,ltp_id, encapsulation, mac, p_status, vlan_id=1, native_vlan=1, ip="", netmask="", vni=1):
        self.cf = CommonFields(name, name)
        self.parentId = ltp_id
        self.connType = self.set_connType(encapsulation)
        self.connInfo = self.set_connInfo(mac, vlan_id, native_vlan, ip, netmask, vni)
        self.status = p_status.upper()

    def to_string(self) -> str:
        result = "{\n\t\t"
        result += self.cf.to_string()
        result += "parent_id: "+self.parent_id+"\n\t\t"
        result += "mac_address: "+self.mac_address+"\n\t\t"
        result += "status: "+self.status+"\n\t\t"
        result += "access_vlan: "+self.vlan_id+"\n\t\t"
        result += "}\n\t\t"
        return result

    def assign_access_vlan(self, vlan:str):
        self.vlan_id = vlan
    
    def set_connType(self, encapsulation):
        switcher = {
                'ARPA': 'Ether', 
                'HDLC': 'IP',
                '802.1Q Virtual LAN': 'IP', 
                'LOOPBACK': 'IP', 
                'Vxlan': 'VXLAN',
                None: 'Ether'
                }
        self.connType = switcher.get(encapsulation,'Ether')

    def set_connInfo(self, mac_address, vlan_id, native_vlan, ip, netmask, vni):
        switcher = {
                'Ether': self.set_etherConnInfo(mac_address, vlan_id, native_vlan),
                'IP': self.set_ipConnInfo(ip, netmask),
                'UDP': self.set_l4ConnInfo(0, 0),
                'TCP': self.set_l4ConnInfo(0, 0),
                'NDN': {},
                'VXLAN': self.set_vxlanConnInfo(vni),
                None: {}
                }
        self.connInfo = switcher[self.connType]
    
    def set_etherConnInfo(self, mac_address, vlan_id, native_vlan):
        self.connInfo = {
                'address': mac_address,
                'vlan':{
                    'vlan_id': vlan_id,
                    'native_vlan': True if vlan_id == native_vlan else False
                    }
                }
    
    def set_ipConnInfo(self, ip, netmask):
        self.connInfo = {
                'address': ip,
                'netmask': netmask
                }

    def set_l4ConnInfo(self, srcPort, destPort):
        self.connInfo = {
                'srcPort': srcPort,
                'destPort': destPort
                }

    def set_vxlanConnInfo(self, vni):
        self.connInfo = {
                'vni': vni
                }

