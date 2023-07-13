import requests
import json
import re

import requests

def create_m3u_playlist(channel_name, channel, playlist_name):
    with open(playlist_name, 'a') as f:
        f.write("#EXTINF:-1 tvg-name=\""+ channel['name'] +"\" tvg-logo=\"" + channel['stream_icon'] + "\"," + channel['name'] + "\n")
        f.write("http://smart.cwdn.cx:80/a804691ee2/12345678/" + str(channel['stream_id']) + "\n")

all_live_url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_live_streams"

all_live_response = requests.request("GET", all_live_url)
live_france = json.loads(all_live_response.text)

channel_name = ""
with open("exports/playlists/all.m3u", 'w') as f:
    f.write("#EXTM3U\n")
for channel in live_france:
    if "FR - " in channel['name']:
        channel_name = re.sub(r'FR - |\[LIVE-EVENT\]|', '', channel["name"]).strip()
        create_m3u_playlist(channel_name, channel, "exports/playlists/all.m3u")