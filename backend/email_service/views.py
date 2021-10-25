import logging
import requests
from django.http import HttpResponse
from github import Github
import os
from django import forms
from pprint import pprint
from django.conf import settings
from .serializers import PullRequestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.mail import EmailMessage
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

@api_view(['GET'])
def detail_via_package(request):
    if request.method == 'GET':
        token = settings.GITHUB_TOKEN
        g = Github(token)
        repo = g.get_repo("georgemjohnson11/auth_system")
        pulls = repo.get_pulls(state="open")
        serializer = PullRequestSerializer(pulls.get_page(0), context={'request': request}, many=True)
        return Response(serializer.data)
    return HttpResponse(f"Hi")

def detail_via_API(request):
    token = settings.GITHUB_TOKEN
    owner = "georgemjohnson11"
    repo = "auth_system"
    query_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    return HttpResponse(r.json())

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contactSubject = form.cleaned_data['contactSubject']
            contactMessage = form.cleaned_data['contactMessage']
            contactEmail = form.cleaned_data['contactEmail']
            authorization = form.cleaned_data['authorization']
            if authorization:
                try:
                    email = EmailMessage(contactSubject, contactMessage, settings.DEFAULT_FROM_EMAIL, contactEmail)
                    email.send()
                except KeyError:
                    return HttpResponse('Please fill in all fields')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/submission/')
    return render(request, "websiteBackbone/contact.html", {'form': form})