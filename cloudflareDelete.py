#!/usr/bin/python
import requests

# Delete IPV4 records
def ipv4RecordDelete(zone, ipv4Zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/"+zone+"/dns_records/"+ipv4Zone
    headers = {
    'X-Auth-Email': CLOUDFLARE_EMAIL,
    'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
    'Cache-Control': "no-cache"
    }
    requests.request("DELETE", url, headers=headers)
    print("IPV4 @ deleted OK")


def ipv4wwwRecordDelete(zone, ipv4wwwZone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv4wwwZone
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    requests.request("DELETE", url, headers=headers)
    print("IPV4 www deleted OK")


# Delete IPV6 records
def ipv6RecordDelete(zone, ipv6Zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/"+zone+"/dns_records/"+ipv6Zone

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

        }

    response = requests.request("DELETE", url, headers=headers)

    print(response.text)


def ipv6wwwRecordDelete(zone, ipv6wwwZone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv6wwwZone
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    requests.request("DELETE", url, headers=headers)
    print("IPV6 www deleted OK")
