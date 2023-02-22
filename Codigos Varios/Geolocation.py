import urllib.request, urllib.parse, urllib.error
import json
import ssl

clave_api = False

if clave_api is False:
    clave_api = 42
    url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'
else :
    url_de_servicio = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    n=1
    direccion = input('Ingresa una ubicacion: ')
    if len(direccion) < 1: break

    parms = dict()
    parms['address'] = direccion
    if clave_api is not False: parms['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(parms)

    print('Recuperando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    print('Recuperados', len(datos), 'caracteres')

    try:
        js = json.loads(datos)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        print(datos)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    code=js['results'][0]["address_components"][len(js['results'][0]["address_components"])-n]['short_name']
    if len(code)==2 and code.isalpha():
        print(code)
    else:
        while len(code)!=2 or code.isnumeric():
            n=n+1
            try:
                code=js['results'][0]["address_components"][len(js['results'][0]["address_components"])-n]['short_name']
                print(code)
            except:
                print('codigo no disponible')
                break