from django.http import HttpResponse
from django.shortcuts import render
import spotipy
import spotipy.util as baba

def index(request):
     return render(request, 'spotifyAuth.html', {}, content_type='text/html')

from django.conf import settings

def getArtistImage(name='Radiohead'):
	spotify = spotipy.Spotify()
	results = spotify.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		artist = items[0]
		return artist['images'][0]['url']

def authorizeSpotify():
	scope = 'user-top-read playlist-modify-private'
	token = baba.prompt_for_user_token('bs672',scope,client_id=settings.SPOTIFY_CLIENT_ID,client_secret=settings.SPOTIFY_CLIENT_SECRET,redirect_uri=settings.BASE_REDIRECT_URL)
	print("HERE eh " + token)
	return token

def getTopTrack(token):
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			return track['name'] + ' - ' + track['artists'][0]['name']
	else:
		return "Can't get token for ", 'bs672'


def index(request):
	# return HttpResponse("<div> fuck </div>")
	return HttpResponse("Hello, world. You're at the polls index.")

def authorize(request):
	token = authorizeSpotify()
	return

def callback(request):
	token = request.GET.get('code')
	print("HERE TOKEN - " + token)
	# top = getTopTrack(token)
	return HttpResponse("TOKEN IS " + token)
