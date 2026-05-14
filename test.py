import os.path
import time
import spotify_credentials
import spotipy
import requests
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_id = spotify_credentials.client_id
client_secret = spotify_credentials.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

print("Success")
print(sys.version)
print("==================================")

artist_id = "3meJIgRw7YleJrmbpbJK6S" #Die drei ???

for i in range(0,20):
    albums = sp.artist_albums(artist_id,offset=i, limit=1)
    time.sleep(1)

    # Folge fetchen
    folgen_name = albums["items"][0]["name"]
    if folgen_name.startswith("Folge"):
        print(folgen_name)
    else:
        print("Folge skiped")
        continue


    #album id und cover fetchen
    album = sp.search(q= folgen_name,type="album", limit=1)
    folgen_name = album["albums"]["items"][0]["name"].replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    album_id = album["albums"]["items"][0]["id"]
    album = sp.album(album_id)
    album_cover = album["images"][1]["url"]

    ordner = "C:\\Users\\Anwender\\Documents\\Obsidian Vault\\Obsidian Vault\\Die drei Fragezeichen"

    # cover speichern
    url = requests.get(album_cover).content
    file_name = os.path.join(ordner + "\\Folgen_cover", folgen_name.replace("/", "_") + ".jpg")
    with open(file_name, "wb") as f:
        f.write(url)
    print("cover gespeichert")

    time.sleep(0.5)
    # release date fetchen und Obsidian properteis erstellen
    release_date = album["release_date"]
    cover_path = ordner + "\\Folgen_cover\\" + folgen_name
    properties = "---\n" + "release_date: " + release_date + "\n" + "cover: \"[[" + folgen_name.replace("/", "_") + ".jpg]]\"\n---"


    file_path = ordner +"\\Folgen\\" + folgen_name.replace("/", "_") + ".md"

    # Folgen Datei speichern
    with open(file_path, "w") as file:
        file.write(properties)
        print("created file")


"""
for i in range(1, 10):
    search_folgen_name = "00" + str(i) + "/und"
    album = sp.search(q= search_folgen_name,type="album", limit=1)
    folgen_name = album["albums"]["items"][0]["name"]
    print("name = " + folgen_name)
    album_id = album["albums"]["items"][0]["id"]
    print("id = " + album_id)
    album = sp.album(album_id)
    album_cover = album["images"][1]["url"]
    print("cover link = " + album_cover)

    ordner = "C:\\Users\\Anwender\\Documents\\Obsidian Vault\\Obsidian Vault\\Die drei Fragezeichen"


    url = requests.get(album_cover).content

    file_name = os.path.join(ordner + "\\Folgen_cover", folgen_name.replace("/", "_") + ".jpg")
    with open(file_name, "wb") as f:
        f.write(url)
    print("gespeichert")

    time.sleep(0.5)

    release_date = album["release_date"]
    cover_path = ordner + "\\Folgen_cover\\" + folgen_name
    properties = "---\n" + "release_date: " + release_date + "\n" + "cover: \"[[" + folgen_name.replace("/", "_") + ".jpg]]\"\n---"


    file_path = ordner +"\\Folgen\\" + folgen_name.replace("/", "_") + ".md"

    with open(file_path, "w") as file:
        file.write(properties)
        print("created file")
"""



