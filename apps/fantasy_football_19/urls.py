from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^matchups$', views.matchups),
    url(r'^teams$', views.teams),
]