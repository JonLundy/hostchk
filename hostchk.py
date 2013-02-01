#!/usr/bin/env python3

import socket, json, subprocess
import urllib.request

hostname = socket.gethostbyaddr(socket.gethostname())[0]

with open('config.json') as f:
  config = json.loads(f.read())

collector_host = config['collector'] + hostname
token = config['token']
host_cfg = []
if hostname in config['hosts']: 
    host_cfg = config['hosts'][hostname]

    store = {} 
    if 'host' in host_cfg: 
        store['host'] = json.loads(subprocess.check_output(['host/host.py']).decode())
    if 'php-fpm' in host_cfg: 
        store['php-fpm'] =  json.loads(subprocess.check_output(['fcgi/fcgi.php']).decode())
    if 'nginx' in host_cfg:
        store['nginx'] =  json.loads(subprocess.check_output(['nginx/nginx.py']).decode())

    urllib.request.urlopen(
        urllib.request.Request(
      	    collector_host,
    	    json.dumps(store).encode(),
    	    headers={
                 'Content-Type': 'application/json',
                 'Authorization': 'token ' + token,
                 }
        )
    )  
