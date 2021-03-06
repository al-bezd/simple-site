# Generated by Django 3.1.3 on 2020-12-20 12:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_blocks.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=50))])), ('list', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(), label='Items'))])), ('image_text_overlay', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))])), ('cropped_images_with_text', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))]), label='Image Item'))])), ('list_with_images', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=200, required=False)), ('link_url', wagtail.core.blocks.URLBlock(label='Link URL', max_length=200, required=False))]), label='List Item'))])), ('thumbnail_gallery', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]), label='Image'))])), ('chart', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Chart Title', label='Title', max_length=120)), ('chart_type', wagtail.core.blocks.ChoiceBlock(choices=[('bar', 'Bar'), ('horizontalBar', 'Horizontal Bar'), ('pie', 'Pie'), ('doughnut', 'Doughnut'), ('polarArea', 'Polar Area'), ('radar', 'Radar'), ('line', 'Line')], label='Chart Type')), ('labels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(default='Label', label='Label', max_length=40), label='Chart Labels')), ('datasets', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(default='Dataset #1', label='Dataset Label', max_length=120)), ('dataset_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.IntegerBlock(), default='0', label='Data'))]), label='Dataset'))])), ('map', wagtail.core.blocks.StructBlock([('marker_title', wagtail.core.blocks.CharBlock(default="Marker Title 'This will be updated after you save changes.'", max_length=120)), ('marker_description', wagtail.core.blocks.RichTextBlock()), ('zoom_level', wagtail.core.blocks.IntegerBlock(default='2', max_value=18, min_value=0, required=False)), ('location_x', wagtail.core.blocks.FloatBlock(default='35.0', required=False)), ('location_y', wagtail.core.blocks.FloatBlock(default='0.16', required=False)), ('marker_x', wagtail.core.blocks.FloatBlock(default='51.5', required=False)), ('marker_y', wagtail.core.blocks.FloatBlock(default='-0.09', required=False))])), ('Badget_list', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('classname', wagtail.core.blocks.CharBlock(label='div class', max_length=200, required=False)), ('name', wagtail.core.blocks.CharBlock(label='name', max_length=200)), ('value', wagtail.core.blocks.CharBlock(label='value', max_length=200))]), label='Items'))])), ('Carousel', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('page', wagtail.core.blocks.PageChooserBlock(required=False))]), label='Image'))])), ('CarouselFull', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('page', wagtail.core.blocks.PageChooserBlock(required=False))]), label='Image'))])), ('Collapsible', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(max_length=120, required=False)), ('name', wagtail.core.blocks.CharBlock(max_length=120)), ('text', wagtail.core.blocks.RichTextBlock(label='text'))]), label='Item'))])), ('Parallax', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'color', 'align', 'align-textol', 'ul', 'hr', 'document-link', 'image', 'embed', 'superscript', 'subscript', 'strikethrough', 'codeblockquote', 'monospace'], required=False))])), ('CKEditor5', wagtail_blocks.blocks.CKEditor5Block()), ('Row', wagtail.core.blocks.StructBlock([('classdiv', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=False)), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('classdiv', wagtail.core.blocks.CharBlock(help_text='s12 m4 l6', max_length=255))]), label='Col'))])), ('Social', wagtail.core.blocks.StructBlock([('view', wagtail.core.blocks.BooleanBlock(default=True, required=True))]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('short_description', wagtail.core.fields.RichTextField()),
                ('description', wagtail.core.fields.RichTextField()),
                ('content', wagtail.core.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogCategories',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
