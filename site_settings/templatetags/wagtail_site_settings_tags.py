

from django import template


from site_settings.models import SocialMediaSettings

register = template.Library()


@register.inclusion_tag('site_settings/social.html')
def social():
    return {'social': SocialMediaSettings.objects.all()[0]}


