from django.db import models

class Github(models.Model):
    class PullRequest(models.Model):
        name = models.CharField(max_length=200)
        description = models.CharField(max_length=200)
        owner = models.CharField(max_length=200)
        publish_date = models.DateTimeField('date published')