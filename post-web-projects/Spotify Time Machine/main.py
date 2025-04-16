import os

import requests
from bs4 import BeautifulSoup
from dotenv import find_dotenv, load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

file = find_dotenv()
load_dotenv(file)

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# USERNAME = os.getenv("USERNAME")


input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

requests = requests.get(url= f"https://www.billboard.com/charts/hot-100/{input_date}", headers=header)
soup = BeautifulSoup( requests.text,"html.parser")

titles = soup.select("li ul h3",class_="lrv-u-width-100p lrv-a-unstyle-list c-title", id="title-of-a-story")

stripped_list = []
for i in titles:
    stripped_list.append(i.text.strip())
print(stripped_list)

scope = "playlist-modify-public"
# auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               username="oq4rzr4dn16e6z727ynhhu8hx",
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri="https://www.billboard.com/charts/hot-100/2000-08-12/"))

playlist = sp.user_playlist_create(user="oq4rzr4dn16e6z727ynhhu8hx",name=f"{input_date} Billboards Top 100 Songs")
#
track_uris = []
playlist_id = playlist['id']

for name in stripped_list:
    x = sp.search(q="track:" + name,type="track",limit=1)
    items = x['tracks']['items'][0]['id']
    # print(items)
    track_uris.append(items)

sp.playlist_add_items(playlist_id=playlist_id,items=track_uris)


