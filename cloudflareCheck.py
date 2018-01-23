#!/usr/bin/python
from cloudflareSearch import *
# def cloudflareCheck(ipv4Record, ipv6Record, ipv6wwwRecord, ipv4wwwRecord, zone, domain,domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
#     if exists != '':
#         if ipv4Record:
#             return ipv4DNSRecordExists == 'True'
#         elif ipv6Record:
#             return ipv6DNSRecordExists == 'True'
#         elif ipv4wwwRecord:
#             return ipv4wwwDNSRecordExists == 'True'
#         elif ipv6wwwRecord:
#             return ipv6wwwDNSRecordExists == 'True'

def ipv4 (ipv4Record, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    return("ipv4DNSRecordExists == 'True'")
def ipv4www (ipv4wwwRecord, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    return("ipv4wwwDNSRecordExists == 'True'")
def ipv6 (ipv6Record, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    return("ipv6DNSRecordExists == 'True'")
def ipv6www (ipv6wwwRecord, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    return("ipv6wwwDNSRecordExists == 'True'")
