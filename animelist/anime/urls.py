from django.urls import path 
from django.http import HttpResponse
from .views import AnimeView, SignupView, LoginView
urlpatterns = [
    path('', AnimeView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
]