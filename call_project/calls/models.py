from django.db import models
from django.core.validators import MinLengthValidator

TYPES = (
    (1, "start"),
    (2, "end")
)


class Call(models.Model):
    """
    Register calls =)
    """
    timestamp = models.DateTimeField(verbose_name="Date")
    type = models.IntegerField(choices=TYPES,
                               verbose_name="Call type")
    call_id = models.IntegerField(verbose_name="Code")
    source = models.CharField(max_length=11, verbose_name="Sender",
                              blank=True, null=True,
                              validators=[MinLengthValidator(10)])
    destination = models.CharField(max_length=11, verbose_name="To",
                                   blank=True, null=True,
                                   validators=[MinLengthValidator(10)])

    def __str__(self):
        return str(self.call_id)

    # Metadata
    class Meta:
        ordering = ["-id"]
        verbose_name = "Call"
