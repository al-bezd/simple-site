
try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock
    wagtail_version = 1
except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock
    wagtail_version = 2

