from queries.send_query import sendQuery

class nodeQuery:
    _os_to_command = {
            'ios':'show lldp neighbors detail',
            'junos':'show lldp neighbors',
            'sonic':'show lldp neighbors',
            'ciena':'show lldp',
            }
    def get_lldp_neighbors(self, target_dev, dev_type, auth_user, auth_pass):
        cmd = "show lldp neighbors detail"
        return sendQuery.run_cmd(target_dev, dev_type, auth_user, auth_pass, cmd)
    
    def build_node_object(self, str_response):
        return None
