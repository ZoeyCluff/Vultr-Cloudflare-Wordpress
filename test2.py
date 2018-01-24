import json
import requests
from variables import *

url = "https://api.cloudflare.com/client/v4/zones/05c841f6ece79182c1f47eea43598432/dns_records"

headers = {
    'X-Auth-Email': CLOUDFLARE_EMAIL,
    'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
    'Cache-Control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
for res in response.json()['result']:

    data = response.json()
    for r in data['result']:
        if r['name'] == 'www.betterpress.site' and r['type'] == 'A':
            ipv4wwwExists = True
            ipv4wwwZone = r['id']

            if ipv4wwwZone != '':
                print("ipv4www =" +ipv4wwwZone)
                # return ipv4wwwZone
            else:
                ipv4wwwZone = False
                # return ipv4wwwZone

        elif r['name'] == 'betterpress.site' and r['type'] == 'A':
            ipv4Exists = True
            ipv4Zone = r['id']
            if ipv4Zone != '':
                print('ipv4 =' + ipv4Zone)
                # return ipv4Zone
            else:
                ipv4Zone = False
                # return ipv4Zone
        elif r['name'] == 'www.betterpress.site' and r['type'] == 'AAAA':
            ipv6wwwExists = True
            ipv6wwwZone = r['id']
            if ipv6wwwZone != '':
                print('ipv6www =' + ipv6wwwZone)
                # return ipv6wwwZone
            else:
                ipv6wwwZone = False
                # return ipv6wwwZone
        elif r['name'] == 'betterpress.site' and r['type'] == 'AAAA':
            ipv6Exists = True
            ipv6Zone = r['id']
            if ipv6Zone != '':
                print('ipv6 =' + ipv6Zone)
                # return ipv6Zone
            else:
                ipv6Zone = False
                # return ipv6Zone
