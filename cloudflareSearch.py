import requests

def zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones"
    querystring = {"name": domain}
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    for res in response.json()['result']:
        if res['name'] == domain:
            zone = res['id']
            return zone


def doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    for res in response.json()['result_info']:
        count = response.json()['result_info']['total_count']
        default = 0
        if count  > default:
            # This should be True rather than a string
            exists = 'true'
            return exists


def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    flat = response.text
    response = requests.request("GET", url, headers=headers)
    for res in response.json()['result']:
    dictonary = json.loads(flat)['result']
    print(dictionary)
        if res['name'] == domain and res['type'] == 'A':
              # ipv4Exists = 'True'
              ipv4Zone = res['']['id'][1]
              print(ipv4Zone)
              return ipv4Zone
    for res in response.json()['result']:
        if res['name'] == domainLong and res['type'] == 'A':
             # ipv4wwwExists = 'True'
             ipv4wwwZone = res['id'][2]
             print(ipv4wwwZone)
             return  ipv4wwwZone

    for res in response.json()['result']:
        if res['name'] == domain and res['type'] == 'AAAA':
             # ipv6Exists = 'True'
             ipv6Zone = res['id']
             print(ipv6Zone)
             return ipv6Zone


    for res in response.json()['result']:
        if res['name'] == domainLong and res['type'] == 'AAAA':
             # ipv6wwwExists = 'True'
             ipv6wwwZone = res['id']
             print(ipv6wwwZone)
             return ipv6wwwZone
