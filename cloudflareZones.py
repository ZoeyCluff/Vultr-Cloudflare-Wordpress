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
    response2 = response['result']


    for r in response2:
        print(r)
        if r['name'] == domain and r['type'] == 'A':
            ipv4Exists = True
            ipv4Zone = r['id']

            if ipv4Zone != '':
                ipv4.append(ipv4Zone)
            else:
                ipv4Zone = False
                ipv4.append(ipv4Zone)


        elif r['name'] == domainLong and r['type'] == 'A':
            ipv4wwwExists = True
            ipv4wwwZone = r['id']

            if ipv4wwwZone != '':

                ipv4www.append(ipv4wwwZone)
            else:
                ipv4wwwZone = False
                ipv4www.append(ipv4wwwZone)


        elif r['name'] == domain and r['type'] == 'AAAA':
            ipv6Exists = True
            ipv6Zone = r['id']

            if ipv6Zone != '':
                ipv6.append(ipv6Zone)
            else:
                ipv6Zone = False
                ipv6.append(ipv6Zone)


        elif r['name'] == domainLong and r['type'] == 'AAAA':
            ipv6wwwExists = True
            ipv6wwwZone = r['id']

            if ipv6wwwZone != '':

                ipv6www.append(ipv6wwwZone)
            else:
                ipv6wwwZone = False
                ipv6www.append(False)


print(ipv4)
print(ipv4www)
print(ipv6)
print(ipv6www)
