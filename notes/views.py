from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import NoteForm
from .models import Note, Tag
from django.views.generic.base import TemplateView


def index(request):
    """Функция возвращает открывшуюся заметку"""
    if request.user.is_authenticated == True:
        user = request.user
        count_notes = len(Note.objects.filter(author=user))
        return render(request, 'notes/index.html', {'count_notes': count_notes})
    return render(request, 'notes/index.html')


@login_required
def show_all_notes(request):
    """Функция возвращает все заметки автора
    page - заметки на 1 странице
    paginator - все заметки разделённые на страницы
    note_list - список всех заметок, одним массивом
    """
    note_list = Note.objects.filter(author__username=request.user.username).all()
    paginator = Paginator(note_list, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'notes/show_all_notes.html', {'page': page,
                                                'paginator': paginator,
                                                'note_list': note_list,
                                                })


@login_required
def show_one_note(request, username, note_id):
    """Функция возвращает открывшуюся заметку"""
    note = get_object_or_404(Note, author__username=username, id=note_id)
    tags = Tag.objects.filter(notes__id=note_id)
    return render(request, 'notes/note.html', {'note': note,
                                               'tags': tags})


@login_required
def note_create(request):
    """Функция создаёт заметки, и сохраняет их"""
    if request.method == 'POST':
        form = NoteForm(request.POST, files=request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(reverse('note:index'))
        return render(request, 'notes/note_create.html', {'form': form})
    form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})


@login_required
def note_edit(request, username, note_id):
    """Функция редактирует существующие заметки"""
    note = get_object_or_404(Note, author__username=username, id=note_id)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect(reverse(
            'note:index', args=[username, note_id]))
    return render(request,
                  'notes/note_create.html',
                  {'form': form, 'note': note})


def page_not_found(request, exception):
    return render(
        request,
        'misc/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(request, 'misc/500.html', status=500)
