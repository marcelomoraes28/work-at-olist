import uuid
import hashlib

from django.db import models

TYPES = (
    (1, "start"),
    (2, "end")
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
    type = models.IntegerField(choices=TYPES,
                               verbose_name="Tipo da ligação")
    call_id = models.ForeignKey('Bill', to_field='call_id',
                                verbose_name="Código",
                                on_delete=models.CASCADE)
    source = models.CharField(max_length=11, verbose_name="Remetente")
    destination = models.CharField(max_length=11, verbose_name="Destinatário")

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = "Chamada"


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
    source = models.CharField(max_length=11, verbose_name="Remetente")
    call_id = models.IntegerField(unique=True, verbose_name="Código")
    call_start_date = models.DateField(verbose_name="Data da Ligação")
    call_start_time = models.TimeField(verbose_name="Horário da Ligação")
    call_price = models.DecimalField(verbose_name="Valor da chamada",
                                     decimal_places=2, max_digits=10,
                                     null=True, blank=True)
    duration = models.TimeField(verbose_name="Duração da Ligação",
                                null=True, blank=True)

    # Metaclass
    class Meta:
        ordering = ["-id"]
        verbose_name = "Conta"
