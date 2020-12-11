
from __future__ import absolute_import, unicode_literals

import json

from bs4 import BeautifulSoup
from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.admin.rich_text.converters.editor_html import DbWhitelister, BASE_WHITELIST_RULES
from wagtail.core.whitelist import Whitelister
from wagtail.utils.widgets import WidgetWithScript
from wagtail.admin.edit_handlers import RichTextFieldPanel
from wagtail.core.rich_text import expand_db_html

from wagtail_ckeditor import settings


class CKEditor(WidgetWithScript, widgets.Textarea):

    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, attrs=None):
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value
                                              # , for_editor=True
                                              )
        return super().render(name, translated_value, attrs)

    def render_js_init(self, editor_id, name, value):

        return "CKEDITOR.replace( '%s', %s);" % (editor_id, mark_safe(json.dumps(settings.WAGTAIL_CKEDITOR_CONFIG)))

    def value_from_datadict(self, data, files, name):
        original_value = super().value_from_datadict(data, files, name)
        if original_value is None:
            return None

        #DbWhitelister.element_rules
        return DbWhitelister(BASE_WHITELIST_RULES).clean(original_value)
