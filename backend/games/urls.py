from django.urls import path
from .views import (
    GameListView, GameDetailView, GenreListView,
    BoardGameListView, BoardGameDetailView
)

urlpatterns = [
    path('games/', GameListView.as_view(), name="game-list"),
    path('games/<int:pk>/', GameDetailView.as_view(), name="game-detail"),
    path('genres/', GenreListView.as_view(), name="genre-list"),
    path('board-games/', BoardGameListView.as_view(), name="board-games-list"),
    path('board-games/<int:pk>/', BoardGameDetailView.as_view(), name="board-game-detail"),
]
