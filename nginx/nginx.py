#!/usr/bin/env python3

# Active connections: 4 
# server accepts handled requests
#  112 112 162 
# Reading: 0 Writing: 1 Waiting: 3 
import socket
import urllib.request
import json

hostname = socket.gethostbyaddr(socket.gethostname())[0]

response = {}
with urllib.request.urlopen('http://' + hostname + '/nginx.status') as f:
    items = f.read().decode().split(' ')
    response = {
         'active'  : {
                'total'  : int(items[2]),
                'reading': int(items[11]),
                'writing': int(items[13]),
                'waiting': int(items[15]),
         },
         'accepts' : int(items[7]),
         'handled' : int(items[8]),
         'requests': int(items[9]),
    }

print(json.dumps(response))
