# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170914_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, help_text='This date is displayed on the blog post. It is not used to schedule posts to go live at a later date.', verbose_name='Post date'),
        ),
    ]
