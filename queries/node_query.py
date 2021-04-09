from queries.send_query import sendQuery

class nodeQuery:   
    def get_lldp_neighbors(self, target_dev, dev_type, auth_user, auth_pass):
        cmd = "show lldp neighbors detail"
        return sendQuery.run_cmd(target_dev, dev_type, auth_user, auth_pass, cmd)
    
    def build_node_object(self, str_response):
        return None
