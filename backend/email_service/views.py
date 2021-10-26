import datetime
import logging
import requests
import json
from django.http import HttpResponse
from github import Github
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime as dt
from django.core.mail import EmailMessage
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# This uses the PyGitHub package
@api_view(['GET'])
def detail_via_package(request):
    if request.method == 'GET':
        token = settings.GITHUB_TOKEN
        g = Github(token)
        repo = g.get_repo("georgemjohnson11/auth_system")
        pulls = repo.get_pulls(state="open")
        # serializer = PullRequestSerializer(pulls.get_page(0), context={'request': request}, many=True)
        return Response(pulls.get_page(0))
    return HttpResponse(f"Hi")

#This is for setting up CORS origin for using a separated frontend
@api_view(['GET'])
def detail_via_React(request):
    token = settings.GITHUB_TOKEN
    owner = "georgemjohnson11"
    repo = "auth_system"
    query_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
    }
    headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    logging.log(r)
    return Response(r.text, headers=headers)

#This is the basic implementation with logic requested
@api_view(['GET'])
def detail_via_API(request, owner, repo):
    errors = ""
    args = {}
    if request.method == "GET":
        try:
            token = settings.GITHUB_TOKEN
            query_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
            seven_days_ago = dt.utcnow() - datetime.timedelta(7)
            params = {
                "state": "all",
            }
            headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Authorization': f'token {token}'}
            r = requests.get(query_url, headers=headers, params=params)
            r_json = json.loads(r.text)
            count = 0
            latest_prs =[]
            if r.ok:
                for pr in r_json:
                    created_date = dt.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    updated_date = dt.strptime(pr['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
                    if created_date > seven_days_ago:
                        message = (f"The pull request '{pr['title']}' at {pr['html_url']} by {pr['user']['login']}")
                        if pr['state'] == 'open':
                            count += 1
                            message+= f" can be reviewed. It was updated at {updated_date}\n"
                        elif pr['closed_at']:
                            count += 1
                            closed_at = dt.strptime(pr['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
                            message += f" has been closed at {closed_at}\n"
                        latest_prs.append(message)
                latest_prs.append(f"\n\nThere's {count} recent pull requests. Please see a summary above\n")
                latest_prs_str = ''.join([i for i in latest_prs])
                context = {'latest_prs': latest_prs, 'latest_prs_str': latest_prs_str}
                return render(request, 'home.html', context)
            else:
                latest_prs = ['There are no recent PRs. Try another repository']
                context = {'latest_prs': latest_prs, 'owner': owner, 'repo': repo}
                return render(request, 'home.html', context)
        except:
            context = {'errors': errors}
            return render(request, 'home.html', context)


@api_view(['GET', 'POST'])
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        contactSubject = form.data['contactSubject']
        contactMessage = form.data['contactMessage_hid']
        contactEmail = form.data['contactEmail']
        authorization = form.data['authorization']
        if authorization == 'on':
            try:
                email = EmailMessage(contactSubject, contactMessage, settings.EMAIL_HOST_USER, [contactEmail])
                email.send()
            except KeyError:
                return HttpResponse('Please fill in all required fields')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/submission/')
    return render(request, "home.html", {'form': form})