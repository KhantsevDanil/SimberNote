from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from django.utils.html import format_html

User = get_user_model()


class Note(models.Model):
    title = models.TextField(verbose_name="about",
                             max_length=15,
                            help_text="what is the note about",)
    tags = models.ManyToManyField("Tag",
                                  related_name="notes",
                                  verbose_name="tags",)
    text = models.TextField(verbose_name="Text",
                            help_text="the main content of the post")
    date_create = models.DateTimeField("Date_create",
                                    auto_now_add=True,
                                    help_text="Date note create")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="notes",
                               verbose_name="author name",
                               help_text="author name")
    image = models.ImageField("Image",
                              upload_to="posts/",
                              blank=True,
                              null=True,
                              help_text="Upload image")

    def __str__(self):
        return (self.text)


class Tag(models.Model):
    """The model describes the tags for fetching by recipes."""
    name = models.CharField("Name", max_length=30)
    hexcolor_regex = RegexValidator(
        regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$',
        message=(
            'Enter valid hex color number'
        )
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        validators=[hexcolor_regex],
        verbose_name='Color'
    )
    slug = models.SlugField(
        "Label", unique=True,
        max_length=200,
        blank=False
    )

    def colored_name(self):
        """Color in format HEX."""
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color,
        )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
