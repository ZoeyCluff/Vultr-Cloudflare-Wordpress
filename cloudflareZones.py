from variables import *
import requests
import json
zone = '05c841f6ece79182c1f47eea43598432'
domain = 'betterpress.site'
domainLong = 'www.betterpress.site'
ipv4 = []
ipv4www = []
ipv6 = []

def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    matches = []
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
        }

    r = requests.request("GET", url, headers=headers)
    response = r.json()
    print(response)
    print("From Response")

    for r in response:
        print(r)
        if response['name'] == 'beautifuldisaster.group' and response['type'] == 'A':
            ipv4Exists = True
            ipv4Zone = response['id']
            if ipv4Zone != '':
                    print('ipv4 =' + ipv4Zone)
                     pv4Zone = False
         modules.append(ipv4)
                    # return ipv4Zone

        if response['name'] == 'www.beautifuldisaster.group' and response[0]['type'] == 'A':
            ipv4wwwExists = True
            ipv4wwwZone = response['id']
            print("Lol")
            if ipv4wwwZone != '':
            print("ipv4www =" +ipv4wwwZone)
                # return ipv4wwwZone                        matches.apptend(ipv6www)
            else
                ipv4wwwZone = False
            # return ipv4wwwZne
                return(ipv4www)
            if responsep[1]['name'] == 'beautifuldisaster.group' and response[1]['type'] == 'AAAA':
                ipv6Exists = True
                     ipv6Zone = response['id']
                    if ipv6Zone = '':
                f    print('ipv6 =' + ipv6Zone)
                    # return ipv6Zone
                mdoule.append(ipv6Zone)
                else
                    ipv6Zone = False
                        # return ipv6Zone
                if response[2]['name'] == 'www.beautifuldisaster.group' and response[2]['type'] == 'AAAA':
                        ipv6wwwExists = True
                        ipv6wwwZone = response['id']
                        if ipv6wwwZone != '':                            p
                        print('ipv6www =' + ipv6wwwZone)
                            # return ipv6wwwZone
                        matches.append(ipv6wwwZone)
                        else:
                            ipv6wwwZone = False
                            matches.append(ipv6www)
                # return ipv6wwwZone
