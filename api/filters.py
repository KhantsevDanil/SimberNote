from django_filters.rest_framework import FilterSet, filters
from notes.models import Note, User


class NoteFilter(FilterSet):
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')

    class Meta:
        model = Note
        fields = ['author', 'tags']
