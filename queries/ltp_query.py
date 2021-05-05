from queries.send_query import sendQuery

class ltpQuery:   
    def get_ltps(target_dev, dev_type, auth_user, auth_pass):
        cmd = "show interface"
        return sendQuery.run_cmd(target_dev, dev_type, auth_user, auth_pass, cmd)
    
    def set_vlan_for_ltp(target_dev, dev_type, auth_user, auth_pass):
        cmd = "show interfaces switchport"
        return sendQuery.run_cmd(target_dev, dev_type, auth_user, auth_pass, cmd)
