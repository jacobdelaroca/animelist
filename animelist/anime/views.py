# from rest_framework
from django.http import JsonResponse
from .models import Anime
from .serializers import AnimeSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AnimeView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # token = requst.data['token']
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]

        anime = Anime.objects.filter(owner=Token.objects.get(key=token).user)
        serializer = AnimeSerializer(anime, many=True)

        return JsonResponse({'anime': serializer.data}, safe=False)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response('Incorrext username or password', status=status.HTTP_404_NOT_FOUND)

        token, c = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({"token": token.key, "user":serializer.data['username']})
    
