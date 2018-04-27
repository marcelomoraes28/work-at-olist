import uuid
import hashlib

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Call


@receiver(post_save, sender=Call)
def generate_call_id(sender, instance, created, **kwargs):
    call = instance
    if created and call.call_id is None:
        call.call_id = hashlib.md5(str(call.id+uuid.uuid4().hex)
                                   .encode('utf-8')).hexdigest()
        call.save()

