import socket
import requests

def get_geoip_info(domain):
    print("\n====== GeoIP Information ======\n")

    try:
        ip = socket.gethostbyname(domain)

        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        print(f"IP Address : {ip}")
        print(f"Country    : {data.get('country')}")
        print(f"Region     : {data.get('regionName')}")
        print(f"City       : {data.get('city')}")
        print(f"ZIP Code   : {data.get('zip')}")
        print(f"ISP        : {data.get('isp')}")
        print(f"Organization : {data.get('org')}")
        print(f"Latitude   : {data.get('lat')}")
        print(f"Longitude  : {data.get('lon')}")
        print(f"Timezone   : {data.get('timezone')}")

    except Exception as e:
        print(f"GeoIP Error: {e}")