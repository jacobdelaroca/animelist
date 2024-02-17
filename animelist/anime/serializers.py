from .models import Anime
from django.contrib.auth.models import User
from rest_framework import serializers

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['name', 'genre', 'rating', 'favorite', 'comment', 'owner']


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']