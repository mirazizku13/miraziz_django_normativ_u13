from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Game
from .forms import GameModelForm

def game_list(request):
    games = Game.objects.all()  # Barcha Productlarni oladi
    return render(request, 'games/list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/detail.html', {'game': game})

def game_create_from(request):
    form = GameModelForm()
    return render(request, 'games/create.html')

def game_create(request):
    if request.method == "POST":
        form = GameModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameModelForm()

    return render(request, 'games/create.html', {'form': form})

def game_update_from(request, pk=None):
    game = Game.objects.filter(pk=pk).first()
    return render(request, 'games/update.html', {'game': game})

def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        form = GameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameModelForm(instance=game)

    return render(request, 'games/update.html', {'form': form})

def game_delete(request, pk=None):
    Game.objects.filter(id=pk).delete()
    return redirect('game_list')