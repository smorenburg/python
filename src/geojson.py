import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = ''
service_url = f'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    if address == 'exit' or address == 'Exit':
        break

    ssl_context = ssl.SSLContext()

    url = service_url + \
        urllib.parse.urlencode({'address': address}) + \
        f'&key={api_key}'

    print(f'Retrieving {url}')
    connection = urllib.request.urlopen(url, context=ssl_context)
    data = connection.read().decode()
    print(f'Retrieved {len(data)} characters')

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(f'\n{json.dumps(json_data, indent=4)}\n')

    lat = json_data['results'][0]['geometry']['location']['lat']
    lng = json_data['results'][0]['geometry']['location']['lng']
    print(f'lat {lat} lng {lng}')
    location = json_data['results'][0]['formatted_address']
    print(location)
