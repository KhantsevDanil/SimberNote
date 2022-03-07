from rest_framework import viewsets

from notes.models import Tag
from api.serializers.tag import TagSerializer
from api.permissions import ReadOnlyOrAdmin

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
