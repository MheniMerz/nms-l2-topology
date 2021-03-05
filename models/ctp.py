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
    def __init__(self, name,ltp_id, encapsulation, mac, p_status, vlan_id=1, native_vlan=1, ip='', netmask='', vni=1):
        self.cf = CommonFields(name, name)
        self.parentId = ltp_id
        self.connType = self.set_connType(encapsulation)
        self.connInfo = self.set_connInfo(mac, vlan_id, native_vlan, ip, netmask, vni)
        self.status = self.normalize_status(p_status)

    def __str__(self):
        result = '{\n\t'
        result += str(self.cf)
        result += 'parent_id: '+str(self.parentId)+'\n\t'
        result += 'ConnType: '+str(self.connType)+'\n\t'
        result += 'ConnInfo: '+str(self.connInfo)+'\n\t'
        result += 'status: '+self.status+'\n'
        result += '}\n'
        return result

    def normalize_status(self, status) -> str:
        status = status.upper()
        if 'DOWN' in status:
            status = 'DOWN'
        elif 'UP' in status:
            status = 'UP'
        else :
            status = 'DISCONN'
        return status

    def assign_access_vlan(self, vlan:str):
        self.vlan_id = vlan
    
    def set_connType(self, encapsulation):
        switcher = {
                'ARPA': 'Ether', 
                'HDLC': 'IPv4',
                '802.1Q Virtual LAN': 'IPv4', 
                'LOOPBACK': 'IPv4', 
                'Vxlan': 'VXLAN'
                }
        return switcher.get(encapsulation.upper(),'Ether')

    def set_connInfo(self, mac_address, vlan_id, native_vlan, ip, netmask, vni):
        switcher = {
                'Ether': self.set_etherConnInfo(mac_address, vlan_id, native_vlan),
                'IPv4': self.set_ipConnInfo(ip, netmask),
                'UDP': self.set_l4ConnInfo(0, 0),
                'TCP': self.set_l4ConnInfo(0, 0),
                'NDN': {},
                'VXLAN': self.set_vxlanConnInfo(vni),
                None: {}
                }
        return switcher[self.connType]
    
    def set_etherConnInfo(self, mac_address, vlan_id, native_vlan):
        return {
                'address': mac_address,
                'vlanId': vlan_id,
                'isNative': True if vlan_id == native_vlan else False
               }
    
    def set_ipConnInfo(self, ip, netmask):
        if ip != '':
            tmp = str.split(ip,'/')
            return {
                    'address': tmp[0],
                    'netmask': tmp[1]
                    }
        return {
                'address': 'N/A',
                'netmask': 'N/A'
                }

    def set_l4ConnInfo(self, srcPort, destPort):
        return {
                'srcPort': srcPort,
                'destPort': destPort
                }

    def set_vxlanConnInfo(self, vni):
        return  {
                'vni': vni
                }

