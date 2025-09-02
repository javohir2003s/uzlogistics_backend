from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from cargo.models import Cargo


def _broadcast(deleted_ids=None):
    layer = get_channel_layer()
    payload = {"type": 'cargos_update'}
    if deleted_ids:
        payload["deleted_ids"] = deleted_ids
    async_to_sync(layer.group_send)("active_cargos", payload)


@receiver(post_save, sender=Cargo)
def cargo_saved(sender, instance, created, **kwargs):
    transaction.on_commit(lambda: _broadcast())

@receiver(post_delete, sender=Cargo)
def cargo_deleted(sender, instance, **kwargs):
    transaction.on_commit(lambda: _broadcast(deleted_ids=[instance.pk]))