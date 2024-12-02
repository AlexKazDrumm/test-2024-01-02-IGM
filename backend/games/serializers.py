from rest_framework import serializers
from .models import Game, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)  # Добавьте это для отладки
        return representation

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'


class BoardGameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    genres = serializers.ListField(child=serializers.CharField())
    players = serializers.CharField()
    min_players = serializers.IntegerField()
    max_players = serializers.IntegerField()
    duration = serializers.CharField()
    image_url = serializers.URLField()