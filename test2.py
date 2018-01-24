import json

json_data = open('test.json').read()

data = json.loads(json_data)



for r in data['result']:
    if r['name'] == 'www.betterpress.site' and r['type'] == 'AAAA':
        print(r['id'])
