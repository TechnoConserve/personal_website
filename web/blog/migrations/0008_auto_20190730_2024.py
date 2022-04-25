# Generated by Django 2.2.3 on 2019-07-31 02:24

import blog.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', blog.models.Heading(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(classname='paragraph', requeried=True)), ('code_chunk', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock(max_length=8000)), ('language', wagtail.core.blocks.ChoiceBlock(choices=[('python', 'Python'), ('django', 'Django'), ('css', 'CSS'), ('http', 'HTTP'), ('javascript', 'JavaScript'), ('bash', 'Bash'), ('dockerfile', 'Dockerfile'), ('ini', 'Ini'), ('sql', 'SQL'), ('json', 'JSON'), ('markdown', 'Markdown'), ('html', 'HTML'), ('xml', 'XML'), ('java', 'Java'), ('nginx', 'Nginx')], required=False))])), ('quote', wagtail.core.blocks.BlockQuoteBlock(help_text='Text to be wrapped in <blockquote> tag pair', required=False))], verbose_name='body'),
        ),
    ]