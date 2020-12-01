import json

class Ctp:
    def __init__(self, name, mac, ip, vlan_id, ltp_id, node_id):
        self.name = name
        self.mac_address = mac
        self.ip_address = ip
        self.vlan_id = vlan_id
        self.ltp_id = ltp_id
        self.node_id = node_id

    def to_string(self) -> str:
        result = "{\n\t\t"
        result += "name: "+self.name+"\n\t\t"
        result += "ip_address: "+self.ip_address+"\n\t\t"
        result += "mac_address: "+self.mac_address+"\n\t\t"
        result += "access_vlan: "+self.vlan_id+"\n\t\t"
        result += "}\n\t\t"
        return result

    def assign_access_vlan(self, vlan:str):
        self.vlan_id = vlan
