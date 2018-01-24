#!/usr/bin/python

import time
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import os
from variables import *
from vultr import *
from cloudflareSearch import zone, doRecordsExist
from cloudflareZones import RecordsExist
# from cloudflareSearch2 import recordsCheck
from cloudflareDelete import ipv4RecordDelete, ipv4wwwRecordDelete, ipv6RecordDelete, ipv6wwwRecordDelete
import sys
import requests
from blessings import Terminal


term = Terminal()


# Create Vultr VPS using default values
print term.red("LetsEncrypt is set to the test API. while certs will be issued, they will not be valid and will display an error. remove --staging from the playbook.yaml file to generate valid certificates.")
# instanceID, ipv4vultr, ipv6vultr = vultr(apikey)

# Doing some Cloudflare checks before continuining.

domain = raw_input("What is the domain name? (without www): ")
domainLong = 'www.' + domain
# zone_id = recordsCheck(domain)
# exists = recordsCheck(domain)
zone = zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
if exists == 'true':
    ipv4Zone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv4wwwZone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6Zone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6wwwZone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
# exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
# TODO - If exists is None, ipv4Record and others will be too.
# Catch the issue here, and sys.exit()
# Proper checks will be implemented later
# if exists is 'True':
    # from cloudflareCheck import *
print("Checking for existing A and AAAA records that may interfere")
if not ipv4Zone:
    print term.yellow("Conflicting ipv4 @ record detected. Site will not function without updating this record. Update?")
    answeripv4 = str(raw_input('Update ipv4 @ records? y/n (lowercase y or n): '))

if not ipv4wwwZone:
    print term.yellow("Conflicting ipv4 www record detected. Site will not function without updating this record. Update?")
    answeripv4WWW = str(raw_input('Update ipv4 www records? y/n (lowercase y or n): '))

if not ipv6Zone:
    print term.yellow("Conflicting ipv6 @ record detected. Site will not function without updating this record. Update?")
    answeripv6 = str(raw_input('Update ipv6 @ records? y/n (lowercase y or n): '))

if not ipv6wwwZone:
    print term.yellow("Conflicting ipv6 www record detected. Site will not function without updating this record. Update?")
    answeripv6WWW = str(raw_input('Update ipv6 www records? y/n (lowercase y or n): '))

# if answeripv4.lower() == 'y':
#     ipv4RecordDelete(zone, ipv4Zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
# if answeripv4WWW.lower() == 'y':
#     ipv4wwwRecordDelete(zone, ipv4wwwZone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
# if answeripv6.lower() == 'y':
#     ipv6RecordDelete(zone, ipv6Zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
#
# if answeripv6WWW.lower() == 'y':
#     ipv6wwwRecordDelete(zone, ipv6wwwZone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)


# Add Cloudflare records
