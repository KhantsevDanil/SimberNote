from django.core.exceptions import ValidationError
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from notes.models import Note, Tag, User


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = Base64ImageField()

    def validate(self, data):
        """Validate
        tags are unique"""
        tags = data['tags']
        existing_tags = {}
        for tag in tags:
            if tag in existing_tags:
                raise ValidationError(
                    'Повторяющиеся теги недопустимы'
                )
            existing_tags['tag'] = True
        return data

    """def create(self, validated_data):
        if 'tag' not in self.initial_data:
            note = Note.objects.create(**validated_data)
            return note
        tags = validated_data.pop('tags')
        note = Note.objects.create(**validated_data)
        for tag in tags:
            current_tag, status = Tag.objects.get_or_create(**tag)
        Notes_to_tag.objects.create(achievement=current_tag,
                                    note=note)
        return note"""

    def create(self, validated_data):
        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
        note = Note.objects.create(**validated_data)
        note.tags.add(*tags)
        return note

    def update(self, instance, validated_data):
        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
            instance.tags.clear()
            instance.tags.add(*tags)
        super().update(instance, validated_data)
        return instance

    class Meta:
        model = Note
        fields = [
            'id',
            'tags',
            'title',
            'image',
            'text',
            'date_create',
            'author'
        ]
