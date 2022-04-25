# Generated by Django 3.1.13 on 2021-11-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CivPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_id', models.CharField(max_length=25)),
                ('discord_id', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CivWebhookMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_at', models.DateTimeField(help_text='When we received the event.')),
                ('payload', models.JSONField(default=None, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='civwebhookmessage',
            index=models.Index(fields=['received_at'], name='civ_civwebh_receive_e00271_idx'),
        ),
    ]