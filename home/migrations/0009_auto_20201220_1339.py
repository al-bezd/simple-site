# Generated by Django 3.1.3 on 2020-12-20 08:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtailimages', '0022_uploadedimage'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('home', '0008_blogсategories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogСategories',
            new_name='BlogCategories',
        ),
    ]
