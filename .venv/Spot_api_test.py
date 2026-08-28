import os.path
import time

import spotipy
import requests
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'ea8555b9a064401ea1ba150d25356081'
client_secret = 'c22ab1bc50f546ee8004db19f5138927'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

print("Success")
print(sys.version)
print("==================================")




#results = sp.search(q="Die drei ???", type="artist", limit=1)

for i in range(1, 10):
    search_folgen_name = "00" + str(i) + "/und"
    album = sp.search(q= search_folgen_name,type="album", limit=1)
    folgen_name = album["albums"]["items"][0]["name"]
    print("name = " + folgen_name)
    album_id = album["albums"]["items"][0]["id"]
    print("id = " + album_id)
    album = sp.album(album_id)
    album_cover = album["images"][0]["url"]
    print("cover link = " + album_cover)

    ordner = "C:/Users/Anwender/Desktop/B_Cover_test"
    file_path = folgen_name.replace("/", "_") + ".txt"

    with open(file_path, "w") as file:
        file.write("test")
        print("created file")

    """
    url = requests.get(album_cover).content

    file_name = os.path.join(ordner, folgen_name.replace("/", "_") + ".jpg")
    with open(file_name, "wb") as f:
        f.write(url)
    print("gespeichert")
    """
    time.sleep(0.5)

"""
album_id = "4BZfSV9maCil4l4yftT74F" #Medusa
artist_id = "3meJIgRw7YleJrmbpbJK6S" #die drei ???

album_info = sp.artist_albums(artist_id, limit=1)
album = sp.album(album_id)
#track_info = sp.artist_albums()
album_cover = album["images"][0]["url"]
print(album_cover)

"""

