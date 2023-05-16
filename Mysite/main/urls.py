from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name= "home"),
path("equipes/", views.equipes, name= "equipes"),
path('templates/', views.enviar_email, name='enviar_email'),
path('overview/', views.overview, name='overview'),
path("conta/", views.conta, name="conta"),
path('phishing/', views.phishing, name="phishing"),
path('sso/', views.sso, name="sso")
]
#start

