import imp
from multiprocessing import context
from multiprocessing.spawn import import_main_path
from django.shortcuts import render

# Create your views here.
from .forms import CreatePoll
from .models import Poll


def home(request):
    return render(request, 'pages/home.html')

def polls(request):
    return render(request, 'pages/polls.html')

def create(request):
    form = CreatePoll()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html',  context)

def vote(request, poll_id):
    context = {}
    return render(request, 'pages/vote.html',  context)


def results(request,  poll_id ):
    context = {}
    return render(request, 'pages/vote.html',  context)