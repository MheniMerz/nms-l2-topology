import json

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
    

class Node:
    def __init__(self, name: str, chassis_id: str, mgmt_ip: str, capability: str):
        self.name = name
        self.chassis_id = chassis_id
        self.mgmt_ip = mgmt_ip
        self.node_type = lldp_capability_to_device_type(capability)
        self.interfaces: dict [str, "Interface"] = {}

    def to_string(self) -> str:
        result  = "{\n\t"
        result += "hostname: "+self.name +"\n\t"
        result += "chassis_id: "+self.chassis_id +"\n\t"
        result += "management_ip: "+self.mgmt_ip +"\n\t"
        result += "device_type: "+ self.node_type +"\n\t"
        result += "interfaces: [\n\t"+self.interfaces_to_string()+"]"
        result += "\n}"
        return result

    def add_interface(self, interface: "Interface") -> None:
        self.interfaces[interface.name] = interface
    
    def interfaces_to_string(self) -> str:
        result = ""
        for k in self.interfaces:
            result += self.interfaces[k].to_string()
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
        return self.name.split(".")[0]

