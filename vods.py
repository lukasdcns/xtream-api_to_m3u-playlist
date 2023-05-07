import requests
import json
import re

url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_vod_streams"

response = requests.request("GET", url)
vods = json.loads(response.text)

for vod in vods:
    if "FR - " in vod['name']:
        vodName = re.sub(r'FR - |:|\/|,|\'|\s*\(\d+\)|\s+', '-', vod["name"])
        vodName = re.sub(r'\([^)]*\)', '', vodName).strip()
        vodName = re.sub(r'--+', '-', vodName)
        vodName = vodName.strip('-').lower()

        vodDateMatch = re.search(r'\((\d{4})\)', vod["name"])
        if vodDateMatch:
            vodDate = vodDateMatch.group(1)

        fileName = "exports/vods/jellyfin/" + vodName + ("-" + vodDate if vodDate else "") + ".strm"
        vodUrl = "http://smart.cwdn.cx:80/movie/a804691ee2/12345678/" + str(vod["stream_id"]) + vod['container_extension']

        with open(fileName, "w") as strm_file:
            strm_file.write(vodUrl)

