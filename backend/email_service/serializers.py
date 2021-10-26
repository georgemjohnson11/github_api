from rest_framework import serializers
from .models import Github

class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Github.PullRequest
        fields = ('name', 'description', 'owner', 'publish_date')