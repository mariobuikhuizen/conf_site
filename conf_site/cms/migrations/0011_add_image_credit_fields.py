# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 20:15
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_homepage_streamfields_are_not_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_credit',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=b''),
        ),
        migrations.AddField(
            model_name='venuepage',
            name='image_credit',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=b''),
        ),
    ]