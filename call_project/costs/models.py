from django.db import models

STATUS = (
    (1, "Ativo"),
    (2, "Inativo")
)

class Cost(models.Model):
    """
    Configuration cost per calls
    """

    created_at = models.DateField(
        verbose_name='Created at',
        auto_now_add=True
    )

    connection_cost = models.FloatField(
        verbose_name="Price of call",
    )

    cost_per_minute = models.FloatField(
        verbose_name='Price per minute',
    )

    initial_period = models.TimeField(
        verbose_name='Start of trading period'
    )

    end_period = models.TimeField(
        verbose_name="End of trading period"
    )
    status = models.IntegerField(choices=STATUS, verbose_name="Status")

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Cost setting'
