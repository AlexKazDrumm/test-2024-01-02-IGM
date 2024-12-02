from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Game, Genre
from .serializers import GameSerializer, GenreSerializer, BoardGameSerializer
from .board_games_data import board_games

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    ordering_fields = ['popularity', 'release_date', 'vote_average']
    filterset_fields = ['genres__name', 'publisher', 'platform']
    pagination_class = StandardResultsSetPagination

class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BoardGameListView(APIView):
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get(self, request):
        query = request.GET.get('query', '').lower()
        sort = request.GET.get('sort', 'title')
        order = request.GET.get('order', 'asc')

        if query:
            filtered_games = [game for game in board_games if query in game['title'].lower()]
        else:
            filtered_games = board_games.copy()

        reverse_order = True if order == 'desc' else False

        if sort == 'min_players':
            filtered_games.sort(key=lambda x: x.get('min_players', 0), reverse=reverse_order)
        elif sort == 'max_players':
            filtered_games.sort(key=lambda x: x.get('max_players', 0), reverse=reverse_order)
        else:
            filtered_games.sort(key=lambda x: x.get('title', '').lower(), reverse=reverse_order)

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(filtered_games, request)
        serializer = BoardGameSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

class BoardGameDetailView(APIView):
    def get(self, request, pk):
        try:
            game = next(game for game in board_games if game['id'] == int(pk))
            serializer = BoardGameSerializer(game)
            return Response(serializer.data)
        except StopIteration:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)