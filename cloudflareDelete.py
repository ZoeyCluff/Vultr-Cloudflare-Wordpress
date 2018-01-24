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
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv6Zone
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    requests.request("DELETE", url, headers=headers)
    print("IPV6 @ deleted OK")


def ipv6wwwRecordDelete(zone, ipv6wwwZone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records/" + ipv6wwwZone
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    requests.request("DELETE", url, headers=headers)
    print("IPV6 www deleted OK")

#
# def deleteRecords(ipv4DNSRecordExists, answerIPV4, zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, ipv4wwwDNSRecordExists, ipv4wwwRecord, answerIPV6, ipv6DNSRecordExists, ipv6Record, ipv6wwwRecord, ipv6wwwDNSRecordExists):
#     if ipv4DNSRecordExists != '':
#         if answerIPV4.lower() == 'y':
#             print("Removing IPV4 A record")
#             ipv4RecordDelete(zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
#     if ipv4wwwDNSRecordExists != '' and answerIPV4 == 'y':
#             print("Removing IPV4 www record")
#             ipv4wwwRecordDelete(zone, ipv4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
#     if ipv6DNSRecordExists != '':
#         if answerIPV6.lower() == 'y':
#             print("Removing IPV6 @ record")
#             ipv6RecordDelete(zone, ipv6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
#     if ipv6wwwDNSRecordExists and answerIPV6 == 'y':
#         print("Removing IPV6 www record")
#         ipv6wwwRecordDelete(zone, ipv6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
