from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import CivPlayer, CivWebhookMessage


class CivPlayerAdmin(ModelAdmin):
    """Civ player admin."""

    model = CivPlayer
    menu_label = "Civ Players"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("steam_id", "discord_id",)
    search_fields = ("steam_id", "discord_id",)


class CivWebhookMessageAdmin(ModelAdmin):
    """Civ webhook message admin."""

    model = CivWebhookMessage
    menu_label = "Civ Webhook Messages"
    menu_icon = "placeholder"
    menu_order = 280
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("received_at", "payload",)
    search_fields = ("payload",)


modeladmin_register(CivPlayerAdmin)
modeladmin_register(CivWebhookMessageAdmin)
