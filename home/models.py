from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, AbstractPage
from wagtail.search import index
from site_settings.blocks import SocialBlock
from this_site.settings import dev
from wagtail_blocks.blocks import default_blocks, RowBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from django.template.defaultfilters import slugify as django_slugify
from django.utils.translation import gettext_lazy as _

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class HomePage(Page):
    body = StreamField(default_blocks() + [
        ('Row', RowBlock()),
        ('Social', SocialBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname=""),
    ]

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogCategories(Page):
    # class Meta:
    #    verbouse_name = "Категория (Блог)"
    intro = RichTextField(blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('image'),
    ]
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

    def get_categories(self):
        return BlogIndexPage.objects.filter(
            # live=True
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('image'),
    ]

    def get_posts(self):
        return self.get_children()
        # return  a

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogPage(Page):
    # title             = models.CharField(max_length=128)
    short_description = RichTextField()
    description = RichTextField()
    content = RichTextField()

    date = models.DateField("Post date")

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('content'),
        index.FilterField('date'),

    ]

    content_panels = Page.content_panels + [
        # FieldPanel('title'),
        FieldPanel('date'),
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('content'),
        ImageChooserPanel('image'),
        # InlinePanel('related_links', label="Related links"),
    ]
    '''
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('image'),
    ]
    '''
    # Parent page / subpage type rules

    # parent_page_types = ['blog.BlogIndex']
    subpage_types = []

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
