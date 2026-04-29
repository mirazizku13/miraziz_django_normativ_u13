from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from accounts.models import UserRole
from accounts.utils import login_required_custom, is_poster, is_moderator
from .models import Game, Status
from .forms import GameModelForm


def game_list(request):
    search = request.GET.get('search','')
    page = request.GET.get('page')
    games = Game.objects.all()
    if request.user.is_authenticated and request.user.role == UserRole.Poster:
        games = games.filter(created_by=request.user)
    elif request.user.is_authenticated and request.user.role == UserRole.Moderator:
        games = games.filter(status=Status.DRAFT)
    else:
        games = games.filter(status=Status.PUBLISHED)
    if search:
        games = games.filter(title__icontains=search)

    paginator = Paginator(games, 5)
    games = paginator.get_page(page)
    return render(request, 'games/game_list.html', {'games': games, 'search': search, 'page': page, 'UserRole': UserRole})

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'games/game_detail.html', {'game': game, 'UserRole': UserRole})

# @is_poster
# def game_create(request):
#     if request.method == 'POST':
#         form = GameModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('games:game_list')
#     else:
#         form = GameModelForm()
#     return render(request, 'games/game_form.html', {'form': form})


@is_poster
def game_create(request):
    form = GameModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            game = form.save(commit=False)
            game.created_by = request.user
            game.save()
            return redirect('games:game_list')
    return render(request, 'games/game_form.html', {'form': form})

@is_poster
def game_update(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        form = GameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:game_list')
    else:
        form = GameModelForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})
@is_poster
def game_delete(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('games:game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})

# @is_moderator
# def game_published(request, pk=None):
#     game = Game.objects.filter(id=pk).first()
#     game.status = Status.PUBLISHED
#     game.save()
#     return redirect('games:game_list')

@is_moderator
def game_published(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.status = Status.PUBLISHED
    game.save()
    return redirect('games:game_list')