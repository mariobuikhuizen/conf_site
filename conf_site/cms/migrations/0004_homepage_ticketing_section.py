# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-21 17:34
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_lengthen_url_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='ticketing_section',
            field=wagtail.wagtailcore.fields.RichTextField(default='<h2>Tickets</h2>'),
        ),
    ]
