# Generated by Django 2.0.4 on 2018-05-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0014_auto_20180518_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='call_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor da chamada'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='duration',
            field=models.TimeField(blank=True, null=True, verbose_name='Duração da Ligação'),
        ),
    ]