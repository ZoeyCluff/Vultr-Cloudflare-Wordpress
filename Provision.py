#!/usr/bin/python

import time
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import os
from variables import *
cf = CloudFlare(CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
from vultr import *
from cloudflareSearch import findZone, doRecordsExist
from cloudflareZones import ipv4Exists, ipv4wwwExists, ipv6Exists, ipv6wwwExists
from cloudflareDelete import ipv4RecordDelete, ipv4wwwRecordDelete, ipv6RecordDelete, ipv6wwwRecordDelete
# from cloudflareDelete import
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

domain = raw_input("What is the domain name? (without www): ")
domainLong = 'www.' + domain
response = cf.get_zone_id(domain)
print(response)

zone = findZone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

if exists == 'true':

    ipv4Zone = ipv4Exists(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv4wwwZone = ipv4wwwExists(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6Zone = ipv6Exists(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)
    ipv6wwwZone = ipv6wwwExists(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong)

    print(ipv4Zone)
    print(ipv4wwwZone)
    print(ipv6Zone)
    print(ipv6wwwZone)
    print("Checking for existing A and AAAA records that may interfere")

    if ipv4 != '':
        print("Conflicting IPv4 @ record detected. Wordpress will not work unless record is updated. Update? (y/n)")
        answeripv4 = str(raw_input('Update ipv4 @ records? y/n (lowercase y or n): '))
        # return answeripv4
    elif ipv4www != '':
        print("Conflicting IPv4 www record detected. Wordpress will not work unless record is updated. Update? (y/n)")
        answeripv4www = str(raw_input('Update ipv4 www records? y/n (lowercase y or n): '))
        # return answeripv4www
    elif ipv6 != '':
        print("Conflicting IPv6 @ record detected. Wordpress will not work unless record is updated. Update? (y/n)")
        answeripv6 = str(raw_input('Update ipv6 @ records? y/n (lowercase y or n): '))
        # return answeripv6
    elif ipv6www != '':
        print("Conflicting IPv6 www record detected. Wordpress will not work unless record is updated. Update? (y/n)")
        answeripv6www = str(raw_input('Update ipv6 www records? y/n (lowercase y or n): '))
        # return answeripv6www
    if answeripv4.lower() == 'y':
        cf.delete_dns_record(domain, domain)
        # cf.create_dns_record('@', domain, ipv4Vultr)

    if answeripv4www.lower() == 'y':
        cf.delete_dns_record(domainLong, domain)
        # cf.create_dns_record('www', domain, ipv4Vultr)

    if answeripv6.lower() == 'y':
        cf.delete_dns_record(domain, domain)
        # cf.update_dns_record(domain, domain, ipv6Vultr, record_type="AAAA")

    if answeripv6www.lower() == 'y':
        cf.delete_dns_record(domainLong, domain)
        # cf.update_dns_record(domainLong, domain, ipv6Vultr, record_type="AAAA")


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
