import os.path
import time
import spotify_credentials
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

# Authentication
client_id = spotify_credentials.client_id
client_secret = spotify_credentials.client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_id = "3meJIgRw7YleJrmbpbJK6S" #Die drei ???

def main():

    offset = 289
    while offset < 308:
        album = get_album(offset)
        #album = get_album_from_name("175/Schattenwelt")
        #album = album["albums"]
        print(get_album_name(album))
        print("offset: " + str(offset))
        if not check_if_main_series(get_album_name(album)):
            print("keine main series Folge; Folge geskippt")
            offset += 1
            continue


        # cover speichern
        album_cover_url = get_album_cover_url(album)
        folgen_name = get_album_name(album)
        ordner = "C:\\Users\\Anwender\\Documents\\Obsidian Vault\\Obsidian Vault\\Die drei Fragezeichen\\Folgen_cover"

        url = requests.get(album_cover_url).content
        file_name = os.path.join(ordner + "\\" + folgen_name.replace("/", "_").replace(":", "_") + ".jpg")
        with open(file_name, "wb") as f:
            f.write(url)
        print("Cover gespeichert")

        folgen_file_path = "C:\\Users\\Anwender\\Documents\\Obsidian Vault\\Obsidian Vault\\Die drei Fragezeichen\\Folgen"
        folgen_file_path = os.path.join(folgen_file_path + "\\" + folgen_name.replace("/", "_").replace(":", "_") + ".md")

        with open(folgen_file_path, "a", encoding="utf8") as file:


            file.write(properties_string_constructor(album))
            file.write(header_string_constructor())
            print("Folge gespeichert")

        offset += 1



def header_string_constructor():
    return "\n" + "### Zusammenfassung" + "\n\n" + "### Handlung" + "\n\n" + "### Gedanken" + "\n\n" + "### Tags" + "\n\n"


def properties_string_constructor(album):

    release_date = "release_date: " + str(get_album_release_date(album))
    track_count = "track_count: " + str(get_album_track_count(album))
    play_time = "play_time: "  + str(get_album_playtime(album))
    album_cover = "cover: \"[[" + str(get_album_name(album).replace("/", "_").replace(":", "_")) +".jpg]]\""

    properties = "---" + "\n" + release_date + "\n" + track_count + "\n" + play_time + "\n" + album_cover + "\n" + "bewertung: 0,0" + "\n" + "---" + "\n"
    print("properties constructed")

    return properties


def find_matching_album(albums, index):
    for i in range(5):
        name = albums["albums"]["items"][i]["name"]
        if name.find(to_three_digit_string(index)) != -1:
            return albums["albums"]["items"][i]["name"]
    return "no match found"

def to_three_digit_string(number):
    if number < 10:
        return "00" + str(number)
    elif number < 100:
        return "0" + str(number)
    else:
        return str(number)

def get_album_from_name(name_suggestion):
    return sp.search(name_suggestion, type="album", limit=10)
time.sleep(0.5)

def get_album_playtime(album):
    number_of_tracks = get_album_track_count(album)
    print("getting play time")
    time_in_seconds = 0
    for i in range(number_of_tracks):
        tracks = sp.album_tracks(get_album_id(album), offset=i, limit=1)
        time.sleep(0.75)
        time_in_ms = tracks["items"][0]["duration_ms"]
        time_in_seconds = time_in_seconds + time_in_ms / 1000
    return int(time_in_seconds / 60)

def check_if_main_series(album_name):
    if album_name.startswith("Folge") or album_name[0].isdigit():
        return True
    else:
        return False



def get_album(offset):


    albums = sp.artist_albums(artist_id, offset=offset, limit=1)
    return albums


def get_album_id(album):
    return album["items"][0]["id"]

def get_album_name(album):

    return album["items"][0]["name"]


def get_album_cover_url(album):
    return album["items"][0]["images"][0]["url"] # [1] = medium resolution 300 * 300

def get_album_track_count(album):
    return album["items"][0]["total_tracks"]

def get_album_release_date(album):
    return album["items"][0]["release_date"]

def print_album_info(album):
    print("name: " + get_album_name(album))
    print("tracks: " + str(get_album_track_count(album)))
    print("runtime: "+ str(get_album_playtime(album)))
    print("release date: " + get_album_release_date(album))
    print("cover url: " + get_album_cover_url(album))
    print("=====================================")

main()
