from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('polls', views.polls, name='polls'),
    path('create', views.create, name='create'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),
]