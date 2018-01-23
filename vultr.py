
#!/usr/bin/python
import requests
import time
from variables import *


# Create Vultr VPS using default values

def vultr(apikey):
    url = 'https://api.vultr.com/v1/server/create'
    headers = {'API-Key': apikey}
    payload = {
        'DCID':DCID,
        'VPSPLANID':VPSPLANID,
        'auto_backups':auto_backups,
        'OSID':OSID,
        'enable_ipv6':enable_ipv6,
        'SSHKEYID': SSHKEYID,
        'FIREWALLGROUPID': FIREWALLGROUPID,
        'label':label,
        'hostname': hostname

    }

    r = requests.post(url, headers=headers, data=payload).json()
    instanceID = r["SUBID"]

    print("VPS Should be created successfully, waiting 60 seconds to provision")
    time.sleep(30)
    # return (instanceID)



    # Get IPV4 address
    url = "https://api.vultr.com/v1/server/list_ipv4"

    querystring = {"SUBID": instanceID}
    # SUBID = querystring["SUBID"]
    headers = {
        'API-Key': apikey,
        'Cache-Control': "no-cache"

    }

    response = requests.get(url, headers=headers, params=querystring).json()


    ipv4vultr = response[instanceID][0]['ip']
    print(ipv4vultr)
    # return (ipv4)


    # Get IPV6 address
    url = "https://api.vultr.com/v1/server/list_ipv6"

    querystring = {"SUBID": instanceID}

    headers = {
        'API-Key': apikey,
        'Cache-Control': "no-cache"

    }

    response = requests.get(url, headers=headers, params=querystring).json()

    ipv6vultr = response[instanceID][0]['ip']
    print(ipv6vultr)
    return (instanceID, ipv4vultr, ipv6vultr)
