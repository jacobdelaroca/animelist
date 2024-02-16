# from rest_framework
from django.http import JsonResponse
from .models import Anime
from .serializers import AnimeSerializer


def viewAll(request):
    anime = Anime.objects.all()
    serializer = AnimeSerializer(anime, many=True)

    return JsonResponse({'anime': serializer.data}, safe=False)