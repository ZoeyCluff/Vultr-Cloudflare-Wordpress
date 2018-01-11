
import requests
import time



# Create Vultr VPS using default values

def vultr(apikey):
    url = 'https://api.vultr.com/v1/server/create'
    headers = {'API-Key': apikey}
    payload = {'DCID': '2', 'VPSPLANID': '201', 'auto_backups': 'yes', 'OSID': '252', 'enable_ipv6': 'yes',
            'SSHKEYID': '57d133b966663', 'FIREWALLGROUPID': 'f3e4770c', 'label': 'letsnotbestupid', 'hostname': 'testlol'}
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
    

    ipv4 = response[instanceID][0]['ip']
   
    # return (ipv4)


    # Get IPV6 address
    url = "https://api.vultr.com/v1/server/list_ipv6"

    querystring = {"SUBID": instanceID}

    headers = {
        'API-Key': apikey,
        'Cache-Control': "no-cache"

    }

    response = requests.get(url, headers=headers, params=querystring).json()
    
    ipv6 = response[instanceID][0]['ip']

    return (instanceID, ipv4, ipv6)
    


