
#!/usr/bin/python
import requests


# Delete IPV4 records
def ipv4RecordDelete(zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/"+zone+"/dns_records/"+ipv4Record

    headers = {
    'X-Auth-Email': CLOUDFLARE_EMAIL,
    'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
    'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV4 @ deleted OK")


def ipv4wwwRecordDelete(zone, ipv4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv4wwwRecord

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV4 www deleted OK")

# Delete IPV6 records


def ipv6RecordDelete(zone, ipv6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv6Record

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV6 @ deleted OK")

def ipv6wwwRecordDelete(zone, ipv6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv6wwwRecord

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    requests.request("DELETE", url, headers=headers)
    print("IPV6 www deleted OK")
