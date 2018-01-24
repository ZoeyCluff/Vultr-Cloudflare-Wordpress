import CloudFlare
import json

def main():
    zone_name = 'betterpress.site'

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
    zone_id = zone['id']
    print(zone_id)

    # request the DNS records from that zone
    try:
        dns_records = cf.zones.dns_records.get(zone_id)
        if dns_records != '':
            exists = True
            for r in dns_records:
                if r['name'] == 'www.betterpress.site' and r['type'] == 'AAAA':
                    print(r['id'])

            return exists
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

    # print the results - first the zone name
    print zone_id, zone_name

    # then all the DNS records for that zone
    for dns_record in dns_records:
        r_name = dns_record['name']
        r_type = dns_record['type']
        r_id = dns_record['id']
        print '\t', r_id, r_name, r_type, r_value

    exit(0)
if __name__ == '__main__':
    main()
