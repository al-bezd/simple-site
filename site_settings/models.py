from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from django import forms
@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = verbose_name
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    color_begin = ColorField(verbose_name='Цвет до наведения')
    color_after = ColorField(verbose_name='Цвет после наведения')
    transition  = models.FloatField(default=1, verbose_name='Время перетекания')

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
            NativeColorPanel('color_begin'),
            NativeColorPanel('color_after'),
            FieldPanel("transition"),
        ], heading= 'Социальные сети')
    ]

@register_setting
class ContactSettings(BaseSetting):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name

    tel1     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №1", verbose_name="Телефон №1")
    tel2     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №2", verbose_name="Телефон №2")
    email    = models.EmailField(blank=True, null=True, verbose_name="Email")

    panels = [
        MultiFieldPanel([
            FieldPanel("tel1"),
            FieldPanel("tel2"),
            FieldPanel("email"),

        ], heading="Контакты")
    ]




#Пока уберу так как задача размыта а объем работы колосальный
'''
@register_setting
class ColorSettings(BaseSetting):
    class Meta:
        verbose_name = 'Цветовая схема'
        verbose_name_plural = verbose_name

    color1 = ColorField()
    color2 = ColorField()
    color3 = ColorField()
    color4 = ColorField()
    color5 = ColorField()

    panels = [
        MultiFieldPanel([
            NativeColorPanel('color1'),
            NativeColorPanel('color2'),
            NativeColorPanel('color3'),
            NativeColorPanel('color4'),
            NativeColorPanel('color5'),

        ], heading="Цветовая схема")
    ]
'''