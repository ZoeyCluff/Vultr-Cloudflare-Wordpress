#!/usr/bin/python
from cloudflareSearch import exists, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY
def cloudflareCheck(exists, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    if exists:
        ipv4DNSRecordExists, ipv4Record = IPV4Record(zone, domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
        ipv4wwwDNSRecordExists, ipv4wwwRecord  = IPV4wwwRecord(zone, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
        ipv6DNSRecordExists, ipv6Record = IPV6Record(zone,  domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
        ipv6wwwDNSRecordExists, ipv6wwwRecord = IPV6wwwRecord(zone,  domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
        return ipv4DNSRecordExists, ipv4Record, ipv4wwwDNSRecordExists, ipv4wwwRecord, ipv6DNSRecordExists, ipv6Record, ipv6wwwDNSRecordExists, ipv6wwwRecord
