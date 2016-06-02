from django.db import models

from markitup.fields import MarkupField
from autoslug import AutoSlugField

from ainow.models import TimestampedModel


class FAQPage(TimestampedModel):
    name = models.CharField(
        max_length=1024,
        help_text='An internal name for this page, to help identify it.',
        blank=True
    )
    title = models.CharField(max_length=1024)
    slug = AutoSlugField(
        db_index=True,
        unique=True,
        editable=True,
        populate_from='title',
        help_text="Used to make a nice url for this FAQ page."
    )
    introduction = MarkupField(blank=True)

    def __str__(self):
        return self.name


class FAQQuestion(TimestampedModel):
    question = models.CharField(max_length=1024)
    slug = AutoSlugField(
        db_index=True,
        unique=True,
        editable=True,
        populate_from='question',
        help_text="Used to make a nice name to link directly to this question."
    )
    answer = MarkupField()
    pages = models.ManyToManyField(
        'FAQPage',
        blank=True,
        related_name='questions'
    )

    def __str__(self):
        return self.question
