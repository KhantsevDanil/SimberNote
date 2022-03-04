from django.urls import path
from .views import (
    note_create,
    note_edit,
    show_all_notes,
    show_one_note,
    index
)

app_name = "note"

urlpatterns = [

    path("", index, name='index'),
    path("all_notes/", show_all_notes, name="all_notes"),
    path("note_create/", note_create, name="note_create"),
    path("<str:username>/<int:note_id>/note/", show_one_note, name="show_one_note"),
    path(
        "<str:username>/<int:note_id>/edit/",
        note_edit,
        name="note_edit"),
]
