import json
import re 


class Ltp:

    LTP_NAME_RE = re.compile(
         r"(?P<ltp_type>[a-zA-Z\-_ ]*)(?P<ltp_num>[\d.\/]*)"
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
    
    def __init__(self, name: str, l_status: str, bandwidth: str, mtu: str, node_id: str):
        self.name = self.normalize_ltp(name)
        self.status = l_status
        self.native_vlan = "1"
        self.bandwidth = bandwidth
        self.mtu = mtu
        self.node = node_id
        self.ctps: dict [str, "Ctp"] = {}

    def to_string(self) -> str:
        result = "{\n\t"
        result += "node: "+self.node+"\n\t"
        result += "name: "+self.name +"\n\t"
        result += "status: "+self.status +"\n\t"
        result += "native_vlan: "+self.native_vlan +"\n\t"
        result += "bandwidth: "+self.bandwidth+"\n\t"
        result += "mtu: "+self.mtu +"\n\t"
        result += "ctps: [\n\t\t"+ self.ctps_to_string()+"]\n\t"
        result += "}\n\t"
        return result

    def add_ctp(self, ctp:"Ctp") -> None:
        self.ctps[ctp.name] = ctp

    def assign_native_vlan(self, vlan:str):
        self.native_vlan = vlan

    def ctps_to_string(self) -> str:
        result =""
        for k in self.ctps:
            result +=self.ctps[k].to_string()
        return result
    
    @staticmethod
    def normalize_ltp(name: str) -> str:
        match = Ltp.LTP_NAME_RE.search(name)
        if match:
            ltp_type = match.group("ltp_type")
            normalized_ltp_type = Ltp.normalize_ltp_type(ltp_type)
            ltp_num = match.group("ltp_num")
            return normalized_ltp_type+ltp_num
        raise ValueError(f"Does not recognize {name} as an ltp name")
    
    @staticmethod 
    def normalize_ltp_type(ltp_type: str) -> str:
        ltp_type = ltp_type.strip().lower()
        for norm_ltp_type in Ltp.NORMALIZED_LTPS:
            if norm_ltp_type.lower().startswith(ltp_type):
                return norm_ltp_type
        return ltp_type
    
