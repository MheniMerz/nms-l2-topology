# nms-l2-topology
this is the IP topology discovery agent for the multiverse network management system

## Overview
[The Multiverse project](https://github.com/multiverse-nms/) aims at providing a feature-rich solution for configuring, monitoring and managing networks.
The topology discovery agent provides the controller with data gathered about network device configurations and connections regardless of vendor, this is acheived by sending CLI commands to extract the state of the network.

## Structure
```bash
.
+-- main.py		//entrypoint
+-- requirements.txt	//dependencies
+-- Dockerfile 
+-- docker-compose.yml 
+-- docker-entrypoint.sh
+-- api			//api client functions
|   +-- api_client.py
|   +-- auth_api.py
|   +-- link_api.py
|   +-- node_api.py
|   +-- ... 
+-- unit_test
|   +-- test_login.py
|   +-- test_ssh.py
|   +-- ... 
+-- models		// scpecifies the schema for retrieved data
|   +-- node.py
|   +-- link.py
|   +-- ltp.py
|   +-- ... 
+-- queries		// defines network queries
|   +-- send_query.py
|   +-- node_query.py
|   +-- ltp_query.py
|   +-- ... 
+-- config		// provides input configuration for the agent
|   +-- config.ini
|   +-- dns_binding.conf 
|   +-- env_vars.conf
```

## Deployment
> Note: for this agent to work properly the multiverse controller needs to be deployed first, if you haven't deployed it yet please refer to the multiverse [deployment guide](https://github.com/multiverse-nms/multiverse-controller#deployment-instructions)

