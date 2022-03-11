from django.contrib import admin

from .models import Note, Tag


class TagInline(admin.TabularInline):
    model = Note.tags.through
    extra = 1
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'


class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'text',
        'date_create',
        'author'
    ]
    search_fields = [
        'text',
    ]
    exclude = [
        'tags',
    ]
    inlines = [
        TagInline,
    ]
    list_filter = [
        'date_create',
        'text',
        'author'
    ]
    empty_value_display = "-пусто-"


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'color',
        'slug',
    ]
    list_filter = [
        'name',
        'color',
    ]
    search_fields = [
        'name',
    ]
    empty_value_display = '-пусто-'


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
