from django.db import models
from calls.models import Call


class Bill(models.Model):
    """
    Bill of users
    """
    destination = models.CharField(max_length=11, verbose_name="To")
    source = models.CharField(max_length=11, verbose_name="Sender")
    call_id = models.IntegerField(unique=True, verbose_name="Code")
    call_start_date = models.DateField(verbose_name="Start call date",
                                       null=True)
    call_start_time = models.TimeField(verbose_name="Start call time",
                                       null=True)
    call_price = models.DecimalField(verbose_name="Cost of call",
                                     decimal_places=2, max_digits=10,
                                     null=True, blank=True)
    duration = models.CharField(verbose_name="Duration time",
                                null=True, blank=True,
                                max_length=9)
    calls = models.ManyToManyField(Call)

    def __str__(self):
        return str(self.call_id)

    # Metaclass
    class Meta:
        ordering = ["-id"]
        verbose_name = "Conta"
