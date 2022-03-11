from rest_framework import viewsets

from api.serializers.tag import TagSerializer
from notes.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
