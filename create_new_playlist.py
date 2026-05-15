import spotify_credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# importiert id und secret aus externer Datei
client_id = spotify_credentials.client_id
client_secret = spotify_credentials.client_secret

# Authentication
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

user_id = "xfza1upwql3d8y93zlokws8xl" #meine id


results = sp.artist("1Ffb6ejR6Fe5IamqA5oRUF")
print(results)