from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .models import Song
from .serializers import SongSerializer
from albums.models import Album

class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return self.queryset.filter(album_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        album = get_object_or_404(Album, pk=pk)
        serializer.save(album=album)
