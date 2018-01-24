from variables import *
import requests
import json

zone = '05c841f6ece79182c1f47eea43598432'
domain = 'betterpress.site'
domainLong = 'www.betterpress.site'

def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)
    flat = response.text
    data = json.loads(flat)
    for i in range(len(data)):
        try:
            for key, value in data['result'][i].items():
                if key == 'name':
                    print value
                    
                    if value == domain:
                        rootRecords
        except:
            pass



test = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
