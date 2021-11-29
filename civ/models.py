from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class CivWebhookMessage(models.Model):
    received_at = models.DateTimeField(help_text="When we received the event.")
    payload = models.JSONField(default=None, null=True)

    panels = [
        FieldPanel('received_at'),
        FieldPanel('payload')
    ]

    class Meta:
        indexes = [
            models.Index(fields=["received_at"]),
        ]


class CivPlayer(models.Model):
    steam_id = models.CharField(max_length=25)
    discord_id = models.CharField(max_length=25)

    panels = [
        FieldPanel('steam_id'),
        FieldPanel('discord_id')
    ]
