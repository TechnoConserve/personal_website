# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-03 18:43
from __future__ import unicode_literals

import blog.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170915_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', blog.models.Heading(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(classname='paragraph', requeried=True)), ('code_chunk', wagtail.core.blocks.StructBlock((('code', wagtail.core.blocks.TextBlock(max_length=8000)), ('language', wagtail.core.blocks.ChoiceBlock(choices=[('python', 'Python'), ('django', 'Django'), ('css', 'CSS'), ('http', 'HTTP'), ('javascript', 'JavaScript'), ('bash', 'Bash'), ('dockerfile', 'Dockerfile'), ('ini', 'Ini'), ('sql', 'SQL'), ('json', 'JSON'), ('markdown', 'Markdown'), ('html', 'HTML'), ('xml', 'XML'), ('java', 'Java'), ('nginx', 'Nginx')], required=False)))))), verbose_name='body'),
        ),
    ]