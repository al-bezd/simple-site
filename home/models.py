from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page

from wagtail_blocks.blocks import default_blocks, RowBlock





class HomePage(Page):
    body = StreamField(default_blocks()+[
        ('Row', RowBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]