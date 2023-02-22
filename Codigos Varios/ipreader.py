import urllib.request, urllib.parse, urllib.error
import json
import ssl
url= 'http://httpbin.org/get'
uh = urllib.request.urlopen(url)
datos = uh.read().decode()
js = json.loads(datos)
lat = js['origin']
print(lat)