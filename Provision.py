#!/usr/bin/python

import time
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import os
from variables import *
cf = CloudFlare(CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
from vultr import *
from cloudflareSearch import zone, doRecordsExist
from cloudflareZones import RecordsExist

from cloudflareDelete2 import 
import sys
import requests
from blessings import Terminal


term = Terminal()


# Create Vultr VPS using default values
print term.red("LetsEncrypt is set to the test API. while certs will be issued, they will not be valid and will display an error. remove --staging from the playbook.yaml file to generate valid certificates.")
instanceID = vultr(apikey)
print(instanceID)
ipv4Vultr, ipv6Vultr = getIPs(instanceID, apikey)
ipv4Vultr = str(ipv4Vultr)
ipv6Vultr = str(ipv6Vultr)
# Doing some Cloudflare checks before continuining.

domain = str(raw_input("What is the domain name? (without www): "))
domainLong = str('www.' + domain)
response = str(cf.get_zone_id(domain))
print(response)

zone = zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
if exists == 'true':
    ipv4Zone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv4wwwZone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6Zone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6wwwZone = RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)

    print("Checking for existing A and AAAA records that may interfere")
    if ipv4Zone is False:
        ipv4Exists = False
    else:
        print term.yellow("Conflicting ipv4 @ record detected. Site will not function without updating this record. Update?")
        answeripv4 = str(raw_input('Update ipv4 @ records? y/n (lowercase y or n): '))
        ipv4Exists = True
    # return ipv4Exists

    if ipv4wwwZone is False:
        ipv4wwwExists = False
    else:
        print term.yellow("Conflicting ipv4 www record detected. Site will not function without updating this record. Update?")
        answeripv4WWW = str(raw_input('Update ipv4 www records? y/n (lowercase y or n): '))
        ipv4wwwExists = True
    #return ipv4wwwExists

    if ipv6Zone is False:
        ipv6Exists = False
    else:
        print term.yellow("Conflicting ipv6 @ record detected. Site will not function without updating this record. Update?")
        answeripv6 = str(raw_input('Update ipv6 @ records? y/n (lowercase y or n): '))
        ipv6Exists = True
    #return ipv6Exists

    if ipv6wwwZone is False:
        ipv6wwwExists = False
    else:
        print term.yellow("Conflicting ipv6 www record detected. Site will not function without updating this record. Update?")
        answeripv6WWW = str(raw_input('Update ipv6 www records? y/n (lowercase y or n): '))
        ipv6wwwExists = True
    # return ipv6wwwExists
    if ipv4Exists and answeripv4.lower() == 'y':
        cf.delete_dns_record(domain, domain)
        cf.create_dns_record('@', domain, ipv4Vultr)

    if ipv4wwwExists and answeripv4WWW.lower() == 'y':
        cf.delete_dns_record(domainLong, domain)
        cf.create_dns_record('www', domain, ipv4Vultr)

    if ipv6Exists and answeripv6.lower() == 'y':
        # cf.delete_dns_record(domain, domain)
        cf.update_dns_record(domain, domain, ipv6Vultr, record_type="AAAA")

    if ipv6wwwExists and answeripv6WWW.lower() == 'y':

        cf.update_dns_record(domainLong, domain, ipv6Vultr, record_type="AAAA")


# Add Cloudflare records

if exists == 'false':
    print term.blue("Adding records to Cloudflare")

    cf.create_dns_record('@', domain, ipv4Vultr)
    cf.create_dns_record('www', domain, ipv4Vultr)
    cf.create_dns_record('@', domain, ipv6Vultr, record_type="AAAA")
    cf.create_dns_record('www', domain, ipv6Vultr, record_type="AAAA")
    print term.green("Cloudflare records added successfully")


print term.blue("Writing ipv4 to Ansible's host file for provisioning.")

with open("./ansible/hosts", 'w') as f:
    f.write("[VPS]" + '\n'+ ipv4Vultr)

print term.magenta("Server created successfully, DNS updated, proceeding to configure the new server as a LEMP host, and downloading and configuring Wordpresss.")
print term.magenta("Invoking Ansible to configure wordpress server, this may take a while.")
print term.magenta("Waiting 30 seconds for any last minute provisioning to finish")

time.sleep(30)

print term.blue("Provisioning host with Ansible")
os.system('ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./ansible/hosts ./ansible/playbook.yaml  --key-file "~/.ssh/id_rsa "')
print term.cyan("server provisioned correctly (in theory), check to make sure page loads correctly with https")
