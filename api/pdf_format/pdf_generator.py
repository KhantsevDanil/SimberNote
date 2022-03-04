from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from notes.models import Note

def notes_list_pdf(user):
    note_list = Note.objects.filter(
        author=user).order_by('-date_create').values(
            'title',
            'tags',
            'text',
            'image',)
    response = HttpResponse(content_type=note_list)
    response['Content-Disposition'] = (
        'attachment; filename="note_list.pdf"'
    )

    page = Canvas(filename=response)
    page.setFont("Helvetica",10)
    page.drawString(210, 800, 'Список покупок')
    page.setFont("Helvetica",10)
    height = 760
    new_page = 0
    for idx, note in enumerate(note_list, start=1):
        new_page += 1
        page.drawString(60, height, text=(
            f'{idx}. {note["title"]}______{note["tags"]} \n'
            f'Текст______\n'
            f'{note["text"]}\n'
            f'{note["image"]}\n'
        ))
        height -= 30
        if new_page == 23:
            page.showPage()
            page.setFont("Helvetica",10)
            height = 760
            new_page = 0
    page.save()
    return response
