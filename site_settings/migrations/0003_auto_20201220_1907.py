# Generated by Django 3.1.3 on 2020-12-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20201217_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsettings',
            name='youtube',
        ),
        migrations.AddField(
            model_name='contactsettings',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactsettings',
            name='tel1',
            field=models.CharField(blank=True, help_text='Телефон №1', max_length=12, null=True, verbose_name='Телефон №1'),
        ),
        migrations.AlterField(
            model_name='contactsettings',
            name='tel2',
            field=models.CharField(blank=True, help_text='Телефон №2', max_length=12, null=True, verbose_name='Телефон №2'),
        ),
    ]
