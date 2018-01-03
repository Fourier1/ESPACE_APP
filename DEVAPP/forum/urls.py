"""DEVAPP URL FORUM
    ecriture des urls de l'application forum
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forum/', views.base, name='base'),

]
