from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Boardgame

def index(request):
    boardgames = Boardgame.objects.order_by('name')[:10]
    template = loader.get_template('boardgames/index.html')
    context = {
        'boardgames': boardgames
    }
    return render(request, 'boardgames/index.html', context)
