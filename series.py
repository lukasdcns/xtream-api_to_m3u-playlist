import requests
import json
import re

url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_series"

response = requests.request("GET", url)
series = json.loads(response.text)

for serie in series:
    if "FR - " in serie['name']:
        serieName = re.sub(r'FR - |:|,|\'|\s*\(\d+\)|\s+', '-', serie["name"])
        serieName = re.sub(r'\([^)]*\)', '', serieName).strip()
        serieName = re.sub(r'--+', '-', serieName)
        serieName = serieName.strip('-').lower()
        print(serieName)

