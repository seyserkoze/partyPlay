import spotipy
from django.conf import settings


def getArtistImage(name='Radiohead'):
	spotify = spotipy.Spotify()
	results = spotify.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
	    artist = items[0]
	    return artist['images'][0]['url']

def authorize(username):
	scope = 'user-top-read playlist-modify-private'
	token = util.prompt_for_user_token(username,scope,client_id=settings.SPOTIFY_CLIENT_ID,client_secret=settings.SPOTIFY_CLIENT_SECRET,redirect_uri=settings.BASE_REDIRECT_URL)
	return token

def getTopTrack(token):
	if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        return track['name'] + ' - ' + track['artists'][0]['name']
	else:
	    return "Can't get token for", username
