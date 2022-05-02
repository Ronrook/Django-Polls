import imp
from multiprocessing import context
from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreatePollForm
from .models import Poll


def home(request):
    # Solicitamos todos los ojetos de la clase Poll y los guardamos 
    polls = Poll.objects.all()
    print('cadena de prueba')
    print(polls)
    # Creamos el contexto con los objetos Poll
    context = {
        'polls':  polls
    }
    #Retornamos la vista Home y le enviamos el contexto
    return render(request, 'pages/home.html', context)



def create(request):
    # Validar si el metodo Http es POST
    if request.method == 'POST':
        # Guardar la peticion
        form = CreatePollForm(request.POST)
        # Validar si es valida
        if form.is_valid():
            form.save()

            return redirect('home')


    else:
        form = CreatePollForm()

    context = {
        'form': form
    }
    return render(request, 'poll/create.html',  context)




def vote(request, poll_id):
    context = {}
    return render(request, 'pages/vote.html',  context)


def results(request,  poll_id ):
    context = {}
    return render(request, 'pages/vote.html',  context)