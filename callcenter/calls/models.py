from django.db import models

TYPES = (
    (1, "Start"),
    (2, "End")
)
STATUS = (
    (1, "Ativo"),
    (2, "Inativo")
)


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


class Call(models.Model):
    """
    Register calls =)
    """
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Data")
    call_type = models.IntegerField(choices=TYPES, verbose_name="Tipo da ligação")
    call_id = models.CharField(max_length=32, verbose_name="Código")
    source = models.CharField(max_length=11, verbose_name="Remetente")
    destination = models.CharField(max_length=11, verbose_name="Destinatário")

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = "Chamada"


class Bill(models.Model):
    """
    Bill of users
    """
    destination = models.CharField(max_length=11, verbose_name="Destinatário")
    call_start_date = models.DateField(verbose_name="Data da Ligação")
    call_start_time = models.TimeField(verbose_name="Horário da Ligação")
    call_price = models.FloatField(verbose_name="Valor da chamada")

    #Metaclass
    class Meta:
        ordering = ["-id"]
        verbose_name = "Conta"
