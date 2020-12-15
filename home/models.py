from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page

from this_site.settings import dev
from wagtail_blocks.blocks import default_blocks, RowBlock





class HomePage(Page):
    body = StreamField(default_blocks()+[
        ('Row', RowBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname=""),
    ]

    '''
    def get_context(self, request, *args, **kwargs):
        context = super(Page, self).get_context(request, *args, **kwargs)


        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context
    '''
    PAGE_TEMPLATE_VAR = 'page'
    def get_context(self, request, *args, **kwargs):
        context = {
            self.PAGE_TEMPLATE_VAR: self,
            'self': self,
            'request': request,
        }

        if self.context_object_name:
            context[self.context_object_name] = self

        context['menuitems'] = Page.objects.filter(
            live=True,
            show_in_menus=True
            )

        return context