from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'spotifyAuth.html', {}, content_type='text/html')