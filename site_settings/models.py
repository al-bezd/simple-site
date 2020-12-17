from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = verbose_name
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading= 'Социальные сети')
    ]

@register_setting
class ContactSettings(BaseSetting):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name

    tel1     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №1")
    tel2     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №2")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("tel1"),
            FieldPanel("tel2"),

        ], heading="Контакты")
    ]