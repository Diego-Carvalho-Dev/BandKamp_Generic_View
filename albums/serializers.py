from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer

class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

