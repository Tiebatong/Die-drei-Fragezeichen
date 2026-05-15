import os.path
import time
import spotify_credentials
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

client_id = spotify_credentials.client_id
client_secret = spotify_credentials.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


artist_id = "3meJIgRw7YleJrmbpbJK6S" #Die drei ???
datei_pfad = "C:\\Users\\Anwender\\Desktop\\Folgennamen_array.txt"


folge = sp.search("003 und der kapartenhund", type="album", limit=1)
folgen_name = folge["albums"]["items"][0]["name"]
print(folgen_name)





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






