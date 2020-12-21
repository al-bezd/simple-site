# Generated by Django 3.1.3 on 2020-12-21 17:46

from django.db import migrations, models
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_colorsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='color_after',
            field=wagtail_color_panel.fields.ColorField(default=1, max_length=7, verbose_name='Цвет после наведения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='color_begin',
            field=wagtail_color_panel.fields.ColorField(default=1, max_length=7, verbose_name='Цвет до наведения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='transition',
            field=models.FloatField(default=1, verbose_name='Время перетекания'),
        ),
    ]