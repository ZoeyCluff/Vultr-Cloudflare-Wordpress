global recordID
global ipv4exist
if ipv4DNSexists:
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
               'X-Auth-Email': CLOUDFLARE_EMAIL}

    querystring = {'type': 'A', 'name': domain}
    r = requests.get(url, headers=headers, params=querystring).json()
   
    for res in r['result']:
        if res['name'] == domain:
            ipv4exist = 'true'

            recordID = res['id']
    print(recordID)
print(recordID)
global recordIDwww
global ipv4wwwexist
if zone:
 
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
               'X-Auth-Email': CLOUDFLARE_EMAIL}

    querystring = {'type': 'A', 'name': domainLong}
    r = requests.get(url, headers=headers, params=querystring).json()
    for res in r['result']:
        if res['name'] == domainLong:
            ipv4wwwexist = 'true'

            recordIDwww = res['id']
    print(recordIDwww)

global record6ID
global ipv6exist
if zone:
  
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
               'X-Auth-Email': CLOUDFLARE_EMAIL}

    querystring = {'type': 'AAAA', 'name': domain}
    r = requests.get(url, headers=headers, params=querystring).json()
    for res in r['result']:
        if res['name'] == domain:
            ipv6exist = 'true'

            record6ID = res['id']
    print(record6ID)
global record6IDwww
global ipv6wwwexist
if zone:
  
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
               'X-Auth-Email': CLOUDFLARE_EMAIL}

    querystring = {'type': 'AAAA', 'name': domainLong}
    r = requests.get(url, headers=headers, params=querystring).json()
    for res in r['result']:
        if res['name'] == domainLong:
            ipv6wwwexist = 'true'

            record6IDwww = res['id']
    print(record6IDwww)
