#!/usr/bin/python

import time
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import os
from variables import *
from vultr import *
from cloudflareSearch import *
from cloudflareDelete import *
from cloudflareCheck import *
import sys
import requests
# Create Vultr VPS using default values
instanceID, ipv4, ipv6 = vultr(apikey)

# Doing some Cloudflare checks before continuining.

domain = str(raw_input("What is the domain name? (without www): "))
domainLong = str('www.' + domain)

zone = zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

exists = doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

# print("Checking for existing A and AAAA records that may interfere")

ipv4DNSRecordExists, ipv4Record, ipv4wwwDNSRecordExists, ipv4wwwRecord, ipv6DNSRecordExists, ipv6Record, ipv6wwwDNSRecordExists, ipv6wwwRecord = cloudflareCheck(exists, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

if exists != '':
    print("Conflicting ipv4 A records detected, site will not be reachable unless you update DNS records with the new server's IP which will cause later steps to fail (the LetsEncrypt cert generation)")
    answerIPV4 = str(raw_input('Update ipv4 records? y/n (lowercase y or n): '))
    print("Conflicting ipv6 AAA records detected, site will not be reachable unless you update DNS records with the new server's IP which will cause later steps to fail (the LetsEncrypt cert generation)")
    answerIPV6 = str(raw_input('Update ipv6 records? y/n (lowercase y/n): '))
    deleteRecords(ipv4DNSRecordExists, answerIPV4, zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, ipv4wwwDNSRecordExists, ipv4wwwRecord, answerIPV6, ipv6DNSRecordExists, ipv6Record, ipv6wwwRecord, ipv6wwwDNSRecordExists)

  
# Add Cloudflare records
print("Adding records to Cloudflare")
cf = CloudFlare(CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
cf.create_dns_record('@', domain, ipv4)
cf.create_dns_record('www', domain, ipv4)
cf.create_dns_record('@', domain, ipv6, record_type="AAAA")
cf.create_dns_record('www', domain, ipv6, record_type="AAAA")
print("Cloudflare records added successfully")


f = open("./ansible/ips.txt", 'w')
f.write("ipv4="+ipv4 + '\n' + "ipv6="+ipv6)
f.close()

print("Writing ipv4 to Ansible's host file for provisioning.")

f = open("./ansible/hosts", 'w')
f.write("[VPS]" + '\n'+ ipv4)
f.close()


print("Server created successfully, DNS updated, proceeding to configure the new server as a LEMP host, and downloading and configuring Wordpresss.")
print("Invoking Ansible to configure wordpress server, this may take a while.")
print("Waiting 30 seconds for any last minute provisioning to finish")

time.sleep(30)

print("Provisioning host with Ansible")
os.system('ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./ansible/hosts ./ansible/playbook.yaml  --key-file "~/.ssh/id_rsa "')
print ("server provisioned correctly (in theory), check to make sure page loads correctly with https")

print("Did server create and provision successfully?")
successAnswer = str(raw_input('Complete successfully and verified the page loads? y/n (lowercase y/n): '))
testing = sys.argv[1]

if successAnswer == 'y' and testing != '':
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

    # print("Checking for existing A and AAAA records that may interfere")

    ipv4DNSRecordExists, ipv4Record, ipv4wwwDNSRecordExists, ipv4wwwRecord, ipv6DNSRecordExists, ipv6Record, ipv6wwwDNSRecordExists, ipv6wwwRecord = cloudflareCheck(exists, zone, domain, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)
   
    if exists != '':
        print("Delete ipv4 records after testing?")
        answerIPV4 = str(raw_input('Update ipv4 records? y/n (lowercase y or n): '))
        print("Delete ipv6 records after testing?")
        answerIPV6 = str(raw_input('Update ipv6 records? y/n (lowercase y/n): '))
        deleteRecords(ipv4DNSRecordExists, answerIPV4, zone, ipv4Record, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, ipv4wwwDNSRecordExists, ipv4wwwRecord, answerIPV6, ipv6DNSRecordExists, ipv6Record, ipv6wwwRecord, ipv6wwwDNSRecordExists)
