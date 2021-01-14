from django.urls import path
from . import views


urlpatterns = [
    path('index', views.get_movie),
]
