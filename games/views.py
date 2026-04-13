from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Game
from .forms import GameModelForm

def game_list(request):
    search = request.GET.get('search', '')
    page = request.GET.get('page')
    games = Game.objects.all()
    if search:
        games = games.filter(title__icontains=search)
    paginator = Paginator(games, 3)
    games = paginator.get_page(page)
    return render(request, 'games/list.html', {'games': games, 'search': search})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/detail.html', {'game': game})

def game_create_from(request):
    form = GameModelForm()
    return render(request, 'games/create.html', {'form': form})

def game_create(request):
        form = GameModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
        return render(request, 'games/create.html', {'form': form})

def game_update_from(request, pk=None):
    game = Game.objects.filter(pk=pk).first()
    return render(request, 'games/update.html', {'game': game})

def game_update(request, pk):
        form = GameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
        return render(request, 'games/update.html', {'form': form})

def game_delete(request, pk=None):
    Game.objects.filter(id=pk).delete()
    return redirect('game_list')