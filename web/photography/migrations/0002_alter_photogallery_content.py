# Generated by Django 3.2.18 on 2023-04-26 02:39

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail_photography.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='content',
            field=wagtail.fields.StreamField([('gallery', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('collection', wagtail_photography.blocks.CollectionChooserBlock())]))], blank=True, use_json_field=True),
        ),
    ]
