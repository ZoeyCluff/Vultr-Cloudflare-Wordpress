
#!/usr/bin/python
import requests
from cloudflareCheck import *




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


def deleteRecords(ipv4DNSRecordExists, zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, ipv4wwwDNSRecordExists, ipv4wwwRecord, ipv6DNSRecordExists, ipv6Record, ipv6wwwRecord, ipv6wwwDNSRecordExists):
    if ipv4DNSRecordExists != '':
        if answerIPV4 == 'y':
            print("Removing IPV4 A record")
            ipv4RecordDelete(zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    if ipv4wwwDNSRecordExists != '' and answerIPV4 == 'y':
            print("Removing IPV4 www record")
            ipv4wwwRecordDelete(zone, ipv4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    if ipv6DNSRecordExists != '':

        if answerIPV6 == 'y':
            print("Removing IPV6 @ record")
            ipv6RecordDelete(zone, ipv6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    if ipv6wwwDNSRecordExists and answerIPV6 == 'y':
        print("Removing IPV6 www record")
        ipv6wwwRecordDelete(zone, ipv6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
