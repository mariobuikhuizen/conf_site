# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-21 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_add_homepage_footer_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='background_image',
            field=models.ForeignKey(blank=True, help_text='Maximum file size is 10 MB', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='logo_image',
            field=models.ForeignKey(blank=True, help_text='Maximum file size is 10 MB', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='venuepage',
            name='background_image',
            field=models.ForeignKey(blank=True, help_text='Maximum file size is 10 MB', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
