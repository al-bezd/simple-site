
try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock
    wagtail_version = 1
except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock
    wagtail_version = 2

"""
class ColSingle(blocks.StructBlock):
    classdiv = blocks.CharBlock(max_length=255, help_text='s12 m4 l6')
    content = StreamField(default_blocks(), blank=True)
    class Meta:
        template = 'wagtail_blocks/col.html'
        # icon = "list-ul"

class RowBlock(blocks.StructBlock):
    classdiv = blocks.CharBlock(max_length=255, help_text='',required=False)
    content  = blocks.ListBlock(
        ColSingle(),
        label="Col",
    )
    class Meta:
        template = 'wagtail_blocks/row.html'
        # icon = "list-ul"
"""