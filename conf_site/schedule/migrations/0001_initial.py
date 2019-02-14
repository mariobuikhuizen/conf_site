# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', wagtail.wagtailcore.fields.StreamField([('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock())], blank=True, help_text='Text to appear on the schedule page.')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'schedule settings',
            },
        ),
    ]
