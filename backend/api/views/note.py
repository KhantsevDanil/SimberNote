from rest_framework import viewsets
from rest_framework.decorators import action

from api.filters import NoteFilter
from api.permissions import IsOwnerOrAdmin
from api.serializers.note import NoteSerializer
from notes.models import Note, Tag, User

from ..pdf_format.pdf_generator import notes_list_pdf


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.select_related('author').all()
    serializer_class = NoteSerializer
    permission_classes = [
        IsOwnerOrAdmin,
    ]
    filterset_class = NoteFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=False,
        methods=['get'],
        url_path='download_all_notes',
        url_name='download_all_notes',
        pagination_class=None,
        permission_classes=[IsOwnerOrAdmin]
    )
    def download_shopping_cart(self, request):
        user = request.user
        return notes_list_pdf(user)
