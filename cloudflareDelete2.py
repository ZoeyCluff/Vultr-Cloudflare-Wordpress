#!/usr/bin/python
import requests
def getRecords(zone, CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY):


    url = "https://api.cloudflare.com/client/v4/zones/"+zone+"/dns_records/"

    headers = {
        'X-Auth-Email': "zoey.cluff@gmail.com",
        'X-Auth-Key': "a39ce681454be1758d7a7ea88753fe42d8cc4",
        'Cache-Control': "no-cache",
        'Postman-Token': "50e98fcb-106c-1f1e-5b63-38884019197d"
        }

    response = requests.request("GET", url, headers=headers)
    print(response.json())['result']
    return response.json()['result']
