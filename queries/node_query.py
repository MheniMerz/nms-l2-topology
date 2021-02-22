from queries.send_query import sendQuery

class nodeQuery:   
    def get_lldp_neighbors(target_dev, dev_type, auth_user, auth_pass):
        cmd = "show lldp neighbors detail"
        return sendQuery.run_cmd(target_dev, dev_type, auth_user, auth_pass, cmd)
