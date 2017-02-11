import json
from c import call
f = open("/home/watashishun/Downloads/www.sis001.com.har")
#f = open('/home/watashishun/Documents/test.json')
j = json.load(f)
wgetArg = ['wget']
for entry in j['log']['entries']:
    r = entry['request']
    url = r['url']
    if url.endswith('.jpg'):
        wgetArg.append(url)
call(wgetArg)
