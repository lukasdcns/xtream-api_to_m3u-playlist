import requests
import json
import re
import os

url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_vod_streams"

response = requests.request("GET", url)
vods = json.loads(response.text)

for vod in vods:
    folderName = ""
    vodName = ""
    if "FR - " in vod['name'] and "HDCAM" not in vod['name']:
        vodName = re.sub(r"FR - |\(VOSTFR\)|\/", "", vod["name"])
        vodName = re.sub(r"\s+", " ", vodName)
        vodName = vodName.replace("VOSTFR", "").replace("vostfr", "")
        vodName += " [tmdbid-{}]".format(vod['tmdb'])
        folderName = "exports/vods/jellyfin/" + vodName
        folderName = folderName.replace("- 4K", "")

        if "4K" in vodName:
            vodName = vodName.replace("- 4K", "- 2160p")
        
        vodUrl = "http://smart.cwdn.cx:80/movie/a804691ee2/12345678/" + str(vod["stream_id"]) + "." + vod['container_extension']
        #fileName = "exports/vods/jellyfin.txt"

        jellyfinVodDir = os.listdir("exports/vods/jellyfin")
        jellyfinVod = [element for element in jellyfinVodDir if os.path.isdir(os.path.join("exports/vods/jellyfin", element))]
        tmdbid = "[tmdbid-"+str(vod['tmdb'])+"]"

        for dir in jellyfinVod:
            if tmdbid in dir:
                folderName = dir
        
        if not os.path.exists(folderName):
            os.makedirs(folderName)

        fileName = folderName + "/" + vodName + ".strm"

        with open(fileName, "w") as strm_file:
            strm_file.write(vodUrl)

