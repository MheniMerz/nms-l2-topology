import paramiko
import time

def connect(known_hosts_file, server_ip, server_port, user, passwd, logger):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_host_key(known_hosts_file)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logger.info('Connecting to' +str(server_ip))
    ssh_client.connect(
            hostname=server_ip,
            port=server_port,
            username=user,
            password=passwd,
            look_for_keys=False,
            allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timout=1, logger):
    logger.info('Sending command: '+command)
    shell.send(command + '\n')
    time.sleep(timout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client, logger):
    if ssh_client.get_transport().is_active() == True:
        logger.info('Closing connection')
        ssh_client.close()

