from django.db import models


class Costs(models.Model):
    STATUS = (
        ("Ativo", 1),
        ("Inativo", 2)
    )

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
    status = models.IntegerField(choices=STATUS)
    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Configuração dos custos'
