# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from apiclient.discovery import build
from apiclient.errors import HttpError
from django.shortcuts import render
import google.oauth2.credentials
import google_auth_oauthlib.flow
from django.shortcuts import redirect

DEVELOPER_KEY = 'AIzaSyCxG6evaIYz09HFaCUyYzUti9WXlGzptBw'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
# Create your views here.
def index(request):
    return render(request,'index.html')

def youtube_fetch(request):
    if request.method == 'GET':
        
        return redirect(authorization_url)
    else:
        return render(request,'index.html')
