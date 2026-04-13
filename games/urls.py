from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),  # detail sahifasi
    path('create-from/', views.game_create_from, name='game_create_from'),
    path('create/', views.game_create, name='game_create'),
    path('update-from/<int:pk>/', views.game_update_from, name='game_update_from'),
    path('update/<int:pk>/', views.game_update, name='game_update'),
    path('delete/<int:pk>/', views.game_delete, name='game_delete'),
]