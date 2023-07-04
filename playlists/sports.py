import requests
import json
import re

import requests

def create_m3u_playlist(channel_name, channel, playlist_name):
    with open(playlist_name, 'a') as f:
        f.write("#EXTINF:-1 tvg-name=\""+ channel['name'] +"\" tvg-logo=\"" + channel['stream_icon'] + "\"," + channel['name'] + "\n")
        f.write("http://smart.cwdn.cx:80/a804691ee2/12345678/" + str(channel['stream_id']) + "\n")


live_categories_url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_live_categories"

categories_response = requests.request("GET", live_categories_url)
live_categories = json.loads(categories_response.text)
live_france_sport_category_id = None

for category in live_categories:
    if category['category_name'] == "|EU| FRANCE SPORTS":
        france_sport_category_id = category['category_id']

live_france_sport_category_url = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_live_streams&category_id=" + str(france_sport_category_id)

live_france_sport_response = requests.request("GET", live_france_sport_category_url)
live_france_sport = json.loads(live_france_sport_response.text)

channel_name = ""
with open("exports/playlists/sports.m3u", 'w') as f:
    f.write("#EXTM3U\n")
for channel in live_france_sport:
    if "FR - " in channel['name']:
        channel_name = re.sub(r'FR - |\[LIVE-EVENT\]|', '', channel["name"]).strip()
        create_m3u_playlist(channel_name, channel, "exports/playlists/sports.m3u")