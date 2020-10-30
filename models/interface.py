import json
import re 

INTERFACE_NAME_RE = re.compile(
     r"(?P<interface_type>[a-zA-Z\-_ ]*)(?P<interface_num>[\d.\/]*)"
 )
 
NORMALIZED_INTERFACES = (
     "FastEthernet",
     "GigabitEthernet",
     "TenGigabitEthernet",
     "FortyGigabitEthernet",
     "Ethernet",
     "Loopback",
     "Serial",
     "Vlan",
     "Tunnel",
     "Portchannel",
     "Management",
)

def normalize_interface(name: str) -> str:
    match = INTERFACE_NAME_RE.search(name)
    if match:
        int_type = match.group("interface_type")
        normalized_int_type = normalize_interface_type(int_type)
        int_num = match.group("interface_num")
        return normalized_int_type+int_num
    raise ValueError(f"Does not recognize {interface_name} as an interface name")

def normalize_interface_type(interface_type: str) -> str:
    int_type = interface_type.strip().lower()
    for norm_int_type in NORMALIZED_INTERFACES:
        if norm_int_type.lower().startswith(int_type):
            return norm_int_type
    return int_type

class Interface:

    def __init__(self, name: str, l_status: str, p_status: str, ip: str, mac: str, node_id: str):
        self.name = normalize_interface(name)
        self.link_status = l_status
        self.protocol_status = p_status
        self.ip_address = ip
        self.mac_address = mac
        self.access_vlan = ""
        self.native_vlan = "1"
        self.node = node_id

    def to_string(self) -> str:
        result = "{\n\t"
        result += "name: "+self.name +"\n\t"
        result += "link_status: "+self.link_status +"\n\t"
        result += "protocol_status: "+self.protocol_status +"\n\t"
        result += "ip_address: "+self.ip_address+"\n\t"
        result += "mac_address: "+self.mac_address+"\n\t"
        result += "access_vlan: "+self.access_vlan +"\n\t"
        result += "native_vlan: "+self.native_vlan +"\n\t"
        result += "node: "+self.node+"\n\t"
        result += "}\n\t"
        return result
    
    def assign_access_vlan(self, vlan:str):
        self.access_vlan = vlan

    def assign_native_vlan(self, vlan:str):
        self.native_vlan = vlan





