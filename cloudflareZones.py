from variables import *
import requests
import json
zone = '05c841f6ece79182c1f47eea43598432'
domain = 'betterpress.site'
domainLong = 'www.betterpress.site'
ipv4 = []
ipv4www = []
ipv6 = []
ipv6www = []
def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }

    r = requests.request("GET", url, headers=headers)
    response = r.json()
    response2 =response['result']

    for r in response2:
        return(ipv4, ipv4www, ipv6, ipv6www)
        if r['name'] == 'betterpress.site' and r['type'] == 'A':
            ipv4Exists = True
            ipv4Zone = r['id']
            if ipv4Zone != '':
                print('ipv4 =' + ipv4Zone)
                ipv4.append(ipv4Zone)


            else:
                ipv4Exists = False
                ipv4.append(ipv4Exists)


        elif r['name'] == 'www.betterpress.site' and r['type'] == 'A':
            ipv4wwwExists = True
            ipv4wwwZone = r['id']
            ipv4www.append(ipv4wwwZone)


            if ipv4wwwZone != '':
                print("ipv4www =" +ipv4wwwZone)


            else:
                ipv4wwwExists = False
                ipv4www.append(ipv4wwwExists)
        elif r['name'] == 'betterpress.site' and r['type'] == 'AAAA':
            ipv6Exists = True
            ipv6Zone = r['id']
            if ipv6Zone != '':
                print('ipv6 =' + ipv6Zone)
                ipv6.append(ipv6Zone)
            else:
                ipv6Exists = False
                ipv6.append(ipv6Exists)
        if r['name'] == 'www.betterpress.site' and r['type'] == 'AAAA':
            ipv6wwwExists = True
            ipv6wwwZone = r['id']
            if ipv6wwwZone != '':
                print('ipv6www =' + ipv6wwwZone)
                ipv6www.append(ipv6wwwZone)
            else:
                ipv6wwwExists = False
                ipv6www.append(ipv6wwwExists)
