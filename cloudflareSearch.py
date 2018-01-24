# import requests
# import simplejson as json
#
#
# def zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
#     url = "https://api.cloudflare.com/client/v4/zones"
#     querystring = {"name": domain}
#     headers = {
#         'X-Auth-Email': CLOUDFLARE_EMAIL,
#         'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
#         'Cache-Control': "no-cache"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     for res in response.json()['result']:
#         if res['name'] == domain:
#             zone = res['id']
#             return zone
#
#
# def doRecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
#     url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
#     headers = {
#         'X-Auth-Email': CLOUDFLARE_EMAIL,
#         'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
#         'Cache-Control': "no-cache"
#     }
#     response = requests.request("GET", url, headers=headers)
#     for res in response.json()['result_info']:
#         count = response.json()['result_info']['total_count']
#         default = 0
#         if count  > default:
#             # This should be True rather than a string
#             exists = 'true'
#             return exists
#
#
# def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong):
#     url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
#     headers = {
#         'X-Auth-Email': CLOUDFLARE_EMAIL,
#         'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
#         'Cache-Control': "no-cache"
#     }
#
#     response = requests.request("GET", url, headers=headers)
#     for res in response.json()['result']:
#         json_data = open('test.json').read()
#
#         data = json.loads(json_data)
#
#
#         for r in data['result']:
#             if r['name'] == domain and r['type'] == 'A':
#                 ipv4Exists = True
#                 ipv4Zone = r['id']
#                 print(ipv4Zone)
#                 #return(ipv4Exists, ipv4Zone)
#             elif r['name'] == domainLong and r['type'] == 'A':
#                 ipv4wwwExists == True
#                 ipv4wwwZone = r['id']
#                 print(ipv4wwwZone)
#                 #return(ipv4wwwExists, ipv4wwwZone)
#             elif r['name'] == domain and r['type'] == 'AAAA':
#                 ipv6Exists = True
#                 ipv6Zone = r['id']
#                 print(ipv6Zone)
#                 #return(ipv6Exists, ipv6Zone)
#             elif r['name'] == domainLong and r['type'] == 'AAAA':
#                 ipv6wwwExists = True
#                 ipv6wwwZone = r['id']
#                 print(ipv6wwwZone)
#                 #return(ipv6wwwExists, ipv6wwwZone
import requests
import CloudFlare

def zone(domain, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    # url = "https://api.cloudflare.com/client/v4/zones"
    # querystring = {"name": domain}
    # headers = {
    #     'X-Auth-Email': CLOUDFLARE_EMAIL,
    #     'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
    #     'Cache-Control': "no-cache"
    # }
    # response = requests.get(url, headers=headers, params=querystring)
    # for res in response.json()['result']:
    #     if res['name'] == domain:
    #         zone = res['id']
    #         return zone
        zone_name = domain

    cf = CloudFlare.CloudFlare()

    # query for the zone name and expect only one value back
    try:
        zones = cf.zones.get(params = {'name':zone_name,'per_page':1})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones.get %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zones.get - %s - api call failed' % (e))

    if len(zones) == 0:
        exit('No zones found')

    # extract the zone_id which is needed to process that zone
    zone = zones[0]
    zone_id = zone['id'
    return(zone_id)

def doRecordsExist(zone_id, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }
    response = requests.get(url, headers=headers)
    for res in response.json()['result_info']:
        count = response.json()['result_info']['total_count']
        default = 0
        if count  > default:
            # This should be True rather than a string
            exists = 'true'
            return exists


def RecordsExist(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY, domain, domainLong):
    url = "https://api.cloudflare.com/client/v4/zones/" + zone + "/dns_records"
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_AUTH_KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.get(url, headers=headers)
    for r in response.json()['result']:

        if r['name'] == domain and r['type'] == 'A':
            ipv4Exists = True
            ipv4Zone = r['id']
            return(ipv4Exists, ipv4Zone)
        elif r['name'] == domainLong and r['type'] == 'A':
            ipv4wwwExists == True
            ipv4wwwZone = r['id']
            return(ipv4wwwExists, ipv4wwwZone)
        elif r['name'] == domain and r['type'] == 'AAAA':
            ipv6Exists = True
            ipv6Zone = r['id']
            return(ipv6Exists, ipv6Zone)
        elif r['name'] == domainLong and r['type'] == 'AAAA':
            ipv6wwwExists = True
            ipv6wwwZone = r['id']
            return(ipv6wwwExists, ipv6wwwZone)
