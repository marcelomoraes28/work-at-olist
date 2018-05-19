from django.db import models


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
