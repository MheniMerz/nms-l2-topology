import json
import re 

LTP_NAME_RE = re.compile(
     r"(?P<interface_type>[a-zA-Z\-_ ]*)(?P<interface_num>[\d.\/]*)"
 )
 
NORMALIZED_LTPS = (
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

def normalize_ltp(name: str) -> str:
    match = LTP_NAME_RE.search(name)
    if match:
        int_type = match.group("ltp_type")
        normalized_int_type = normalize_ltp_type(int_type)
        int_num = match.group("ltp_num")
        return normalized_int_type+int_num
    raise ValueError(f"Does not recognize {name} as an interface name")

def normalize_ltp_type(ltp_type: str) -> str:
    int_type = ltp_type.strip().lower()
    for norm_int_type in NORMALIZED_LTPS:
        if norm_int_type.lower().startswith(int_type):
            return norm_int_type
    return int_type

class Ltp:

    def __init__(self, name: str, l_status: str, p_status: str, ip: str, mac: str, node_id: str):
        self.name = normalize_ltp(name)
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





