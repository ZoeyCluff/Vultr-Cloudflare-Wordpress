
#!/usr/bin/python
import requests
from cloudflareSearch import *


# Delete IPV4 records
def ipv4RecordDelete(zone, IPV4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + IPV4Record

    headers = {
    'X-Auth-Email': CLOUDFLARE_EMAIL,
    'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
    'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV4 @ deleted OK")


def ipv4wwwRecordDelete(zone, IPV4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + IPV4wwwRecord

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV4 www deleted OK")

# Delete IPV6 records


def ipv6RecordDelete(zone, IPV6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + IPV6Record

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV6 @ deleted OK")

def ipv6wwwRecordDelete(zone, IPV6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + IPV6wwwRecord

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV6 www deleted OK")
