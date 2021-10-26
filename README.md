# github_api

Using GitHub API to retrieve a summary of all pull requests(PRs) for a given repository:   
These should be from the last week   
these should be opened, closed, or in-progress PRs   

## Prerequisites
Get a [Github Token](https://github.com/settings/apps)
Get a [Google Auth Token](https://developers.google.com/gmail/api/auth/about-auth)
Python3 and Pip3

The Github Token will need to go into settings.py as `GITHUB_TOKEN`   
The Google Gmail Password will replace `EMAIL_HOST_PASSWORD` with `EMAIL_HOST_USERNAME` would be your Gmail username

## Setup   
Using Python: 
```
cd backend/   
pip3 install -r requirements.txt   
python3 manage.py runserver 127.0.0.1:8000
```
using Docker: 
```
docker build -t github_api .
docker run -d -p 8000:8000  --name github_api github_api\
--name github_api github_api
```
To get information about a repository visit `localhost:8000/api/owner/repo/` where the `owner` of a repository
is the Github Username and the `repo` is the repository name. For example, this repository could be accessed at: 
`localhost:8000/api/georgemjohnson11/github_api/`   
   
Note: The trailing slash is important