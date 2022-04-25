import datetime as dt
import json
import logging

import requests
from django.conf import settings
from django.db.transaction import non_atomic_requests, atomic
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from civ.models import CivWebhookMessage, CivPlayer

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
@non_atomic_requests
def civ_webhook(request):
    CivWebhookMessage.objects.filter(
        received_at__lte=timezone.now() - dt.timedelta(days=7)
    ).delete()
    payload = json.loads(request.body)
    CivWebhookMessage.objects.create(
        received_at=timezone.now(),
        payload=payload,
    )
    process_webhook_payload(payload)
    return HttpResponse("Message received okay.", content_type="text/plain")


@atomic
def process_webhook_payload(payload):
    try:
        game_name = payload['value1']
        player_name = payload['value2']
        turn_num = payload['value3']
    except KeyError:
        logger.error(f"Invalid payload {payload}")
        return

    try:
        player = CivPlayer.objects.get(steam_id=player_name)
    except CivPlayer.DoesNotExist:
        logger.error(f"CivPlayer object with steam name {player_name} does not exist.")
        return

    response_payload = {"content": f"<@{player.discord_id}> It is your turn ({turn_num}) to move in {game_name}"}
    requests.post(settings.DISCORD_WEBHOOK_URL, json=response_payload)
