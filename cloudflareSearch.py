import requests
from collections import Counter


def zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones"


    querystring = {"name": domain}

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    for res in response.json()['result']:
        if res['name'] == domain:
            zone = res['id']
            return zone


def doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"

    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"

    }

    response = requests.request("GET", url, headers=headers)
    for res in response.json()['result_info']:
        count = response.json()['result_info']['total_count']

        default = int('0')
        if count  > default:
            exists = 'true'
            return exists


def IPV4Record(zone, domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    if zone:

        url = "https://api.cloudflare.com/client/v4/zones/"+zone+"/dns_records"

        querystring = {"type": "A", "name": domain}

        headers = {
            'X-Auth-Email': CLOUDFLARE_EMAIL,
            'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
            'Cache-Control': "no-cache"

        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        for res in response.json()['result']:
            if res['name'] == domain:
                ipv4DNSRecordExists = 'true'
                ipv4Record = res['id']
                return (ipv4DNSRecordExists, ipv4Record)


def IPV4wwwRecord(zone, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    if zone:

        url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"

        querystring = {"type": "A", "name": domainLong}

        headers = {
            'X-Auth-Email': CLOUDFLARE_EMAIL,
            'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
            'Cache-Control': "no-cache"

        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        for res in response.json()['result']:
            if res['name'] == domainLong:
                ipv4wwwDNSRecordExists = 'true'
                ipv4wwwRecord = res['id']
                return (ipv4wwwDNSRecordExists, ipv4wwwRecord)


def IPV6Record(zone, domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    if zone:

        url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"

        querystring = {"type": "AAAA", "name": domain}

        headers = {
            'X-Auth-Email': CLOUDFLARE_EMAIL,
            'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
            'Cache-Control': "no-cache"

        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        for res in response.json()['result']:
            if res['name'] == domain:
                ipv6DNSRecordExists = 'true'
                ipv6Record = res['id']
                return (ipv6DNSRecordExists, ipv6Record)


def IPV6wwwRecord(zone, domainLong, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    if zone:

        url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"

        querystring = {"type": "AAAA", "name": domainLong}

        headers = {
            'X-Auth-Email': CLOUDFLARE_EMAIL,
            'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
            'Cache-Control': "no-cache"

        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        for res in response.json()['result']:
            if res['name'] == domainLong:
                ipv6wwwDNSRecordExists = 'true'
                ipv6wwwRecord = res['id']

                return (ipv6wwwDNSRecordExists, ipv6wwwRecord)
