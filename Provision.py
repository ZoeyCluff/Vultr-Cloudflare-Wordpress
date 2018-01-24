#!/usr/bin/python

import time
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import os
from variables import *
from vultr import *
from cloudflareSearch import zone, doRecordsExist, IPV4Record, IPV4wwwRecord, IPV6Record, IPV6wwwRecord
from cloudflareDelete import ipv4RecordDelete, ipv4wwwRecordDelete, ipv6RecordDelete, ipv6wwwRecordDelete

import sys
import requests
from blessings import Terminal

term = Terminal()


# Create Vultr VPS using default values
print term.red("LetsEncrypt is set to the test API. while certs will be issued, they will not be valid and will display an error. remove --staging from the playbook.yaml file to generate valid certificates.")
instanceID, ipv4vultr, ipv6vultr = vultr(apikey)

# Doing some Cloudflare checks before continuining.

domain = raw_input("What is the domain name? (without www): ")
domainLong = 'www.' + domain

zone = zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
exists = doRecordsExist(zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
# exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
# TODO - If exists is None, ipv4Record and others will be too.
# Catch the issue here, and sys.exit()
# Proper checks will be implemented later
if exists is 'True':
    # from cloudflareCheck import *
    if ipv4Exists:
        ipv4DNSRecordExists, ipv4Record = IPV4Record(zone, domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
        print(ipv4Exists)
    elif ipv4wwwExists:
        ipv4wwwDNSRecordExists, ipv4wwwRecord  = IPV4wwwRecord(zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    elif ipv6Exists:
        ipv6DNSRecordExists, ipv6Record = IPV6Record(zone,  domain,  CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    elif ipv6wwwExists:
        ipv6wwwDNSRecordExists, ipv6wwwRecord = IPV6wwwRecord(zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    print("Checking for existing A and AAAA records that may interfere")
    if ipv4Record:
        print term.yellow("Conflicting ipv4 @ record detected. Site will not function without updating this record. Update?")
        answeripv4 = str(raw_input('Update ipv4 @ records? y/n (lowercase y or n): '))

    if ipv4wwwRecord:
        print term.yellow("Conflicting ipv4 www record detected. Site will not function without updating this record. Update?")
        answeripv4WWW = str(raw_input('Update ipv4 www records? y/n (lowercase y or n): '))

    if ipv6Record:
        print term.yellow("Conflicting ipv6 @ record detected. Site will not function without updating this record. Update?")
        answeripv6 = str(raw_input('Update ipv6 @ records? y/n (lowercase y or n): '))

    if ipv6wwwRecord:
        print term.yellow("Conflicting ipv6 www record detected. Site will not function without updating this record. Update?")
        answeripv6WWW = str(raw_input('Update ipv6 www records? y/n (lowercase y or n): '))

    if answeripv4.lower() == 'y':
        ipv4RecordDelete(zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    if answeripv4WWW.lower() == 'y':
        ipv4wwwRecordDelete(zone, ipv4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    if answeripv6.lower() == 'y':
        ipv6RecordDelete(zone, ipv6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    if answeripv6WWW.lower() == 'y':
        ipv6wwwRecordDelete(zone, ipv6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)


# Add Cloudflare records
print term.blue("Adding records to Cloudflare")
cf = CloudFlare(CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
cf.create_dns_record('@', domain, ipv4vultr)
cf.create_dns_record('www', domain, ipv4vultr)
cf.create_dns_record('@', domain, ipv6vultr, record_type="AAAA")
cf.create_dns_record('www', domain, ipv6vultr, record_type="AAAA")
print term.green("Cloudflare records added successfully")

with open("./instances.py", 'a') as f:
    f.write(instanceID)

with open("./ips.txt", 'w') as f:
    f.write("ipv4="+ipv4vultr + '\n' + "ipv6="+ipv6vultr)

print term.blue("Writing ipv4 to Ansible's host file for provisioning.")

with open("./ansible/hosts", 'w') as f:
    f.write("[VPS]" + '\n'+ ipv4vultr)

print term.magenta("Server created successfully, DNS updated, proceeding to configure the new server as a LEMP host, and downloading and configuring Wordpresss.")
print term.magenta("Invoking Ansible to configure wordpress server, this may take a while.")
print term.magenta("Waiting 30 seconds for any last minute provisioning to finish")

time.sleep(30)

print term.blue("Provisioning host with Ansible")
os.system('ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./ansible/hosts ./ansible/playbook.yaml  --key-file "~/.ssh/id_rsa "')
print term.cyan("server provisioned correctly (in theory), check to make sure page loads correctly with https")

print term.red("Did server create and provision successfully?")
successAnswer = str(raw_input('Complete successfully and verified the page loads? y/n (lowercase y/n): '))
testing = sys.argv[1]

if successAnswer.lower() == 'y' and testing != '':
    headers = {
    'API-Key': apikey,
    }

    data = [
  ('SUBID', instanceID),
    ]

    response = requests.post('https://api.vultr.com/v1/server/destroy', headers=headers, data=data)
    print("VPS should be destroyed")

    print("Deleting Cloudflare records")
    exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    ipv4DNSRecordExists, ipv4Record = IPV4Record(zone, domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv4wwwDNSRecordExists, ipv4wwwRecord  = IPV4wwwRecord(zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv6DNSRecordExists, ipv6Record = IPV6Record(zone,  domain,  CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv6wwwDNSRecordExists, ipv6wwwRecord = IPV6wwwRecord(zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv4RecordDelete(zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv4wwwRecordDelete(zone, ipv4wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv6RecordDelete(zone, ipv6Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
    ipv6wwwRecordDelete(zone, ipv6wwwRecord, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
