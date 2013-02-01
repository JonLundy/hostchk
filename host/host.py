#!/usr/bin/env python3
import os
import json
import psutil
import socket
from datetime import datetime, timedelta

hostname = socket.gethostbyaddr(socket.gethostname())[0]

print(json.dumps({
    'hostname' : hostname,
    'loadavg'  : os.getloadavg(),
    'uptime'   : (datetime.now() - datetime.fromtimestamp(psutil.BOOT_TIME)).total_seconds(),
    'memory' : {
       'total'   : str(psutil.virtual_memory().total),
       'available': str(psutil.virtual_memory().available),
    },
    'swap' : {
        'total' : str(psutil.swap_memory().total),
        'available'  : str(psutil.swap_memory().free),  
    }  
}))
