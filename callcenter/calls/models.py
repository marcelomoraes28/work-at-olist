import uuid
import hashlib

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from .tasks import generate_bill

TYPES = (
    (1, "Start"),
    (2, "End")
)
STATUS = (
    (1, "Ativo"),
    (2, "Inativo")
)


class Call(models.Model):
    """
    Register calls =)
    """
    timestamp = models.DateTimeField(verbose_name="Data")
    call_type = models.IntegerField(choices=TYPES, verbose_name="Tipo da ligação")
    call_id = models.IntegerField(verbose_name="Código")
    source = models.CharField(max_length=11, verbose_name="Remetente")
    destination = models.CharField(max_length=11, verbose_name="Destinatário")

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = "Chamada"


@receiver(post_save, sender=Call)
def generate_call_id(sender, instance, created, **kwargs):
    """
    Signal do generate a call_id
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    call = instance
    if created and call.call_id is "":
        call.call_id = hashlib.md5(str(str(call.id)+uuid.uuid4().hex)
                                   .encode('utf-8')).hexdigest()
        call.save()
    elif created and call.call_id:
        start = Call.objects\
            .filter(call_type=TYPES[0][0], call_id=call.call_id).last()
        call.source = start.source
        call.destination = start.destination
        call.save()
        generate_bill.delay(call.call_id)


class Cost(models.Model):
    """
    Configuration cost per calls
    """
    created_at = models.DateField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    connection_cost = models.FloatField(
        verbose_name="Valor por ligação",
    )

    cost_per_minute = models.FloatField(
        verbose_name='Valor por minuto',
    )

    initial_period = models.TimeField(
        verbose_name='Início do período comercial'
    )

    end_period = models.TimeField(
        verbose_name="Final do período comercial"
    )
    status = models.IntegerField(choices=STATUS, verbose_name="Situação")

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Configuração dos custos'


class Bill(models.Model):
    """
    Bill of users
    """
    destination = models.CharField(max_length=11, verbose_name="Destinatário")
    call_id = models.CharField(max_length=32, verbose_name="Código",
                               null=True, blank=False)
    call_start_date = models.DateField(verbose_name="Data da Ligação")
    call_start_time = models.TimeField(verbose_name="Horário da Ligação")
    call_price = models.FloatField(verbose_name="Valor da chamada")
    duration = models.TimeField(verbose_name="Duração da Ligação",
                                null=True)

    #Metaclass
    class Meta:
        ordering = ["-id"]
        verbose_name = "Conta"
