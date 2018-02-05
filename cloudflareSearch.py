import requests
import json


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
            exists = True
            return exists
        else:
            exists = False
            return exists
