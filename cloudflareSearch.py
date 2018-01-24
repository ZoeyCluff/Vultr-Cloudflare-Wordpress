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

    response = requests.request("GET", url, headers=headers)

    # for res in response.json()['result']:
for r in response.json()['result']:
    if r['name'] == domain and r['type'] == 'A':
        ipv4Exists = True
        ipv4Zone = r['id']
        return(ipv4Exists, ipv4Zone)
    elif r['name'] == domainLong and r['type'] == 'A':
        ipv4wwwExists == True
        ipv4wwwZone = r['id']
        return(ipv4wwwExists, ipv4wwwZone)
    elif r['name'] == domain and r['type'] == 'AAAA':
        ipv6Exists = True
        ipv6Zone = r['id']
        return(ipv6Exists, ipv6Zone)
    elif r['name'] == domainLong and r['type'] == 'AAAA':
        ipv6wwwExists = True
        ipv6wwwZone = r['id']
        return(ipv6wwwExists, ipv6wwwZone)
