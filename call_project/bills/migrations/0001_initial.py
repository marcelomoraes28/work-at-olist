# Generated by Django 2.0.4 on 2018-05-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=11, verbose_name='Destinatário')),
                ('source', models.CharField(max_length=11, verbose_name='Remetente')),
                ('call_id', models.IntegerField(unique=True, verbose_name='Código')),
                ('timestamp', models.DateTimeField(verbose_name='Data da Ligação')),
                ('call_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor da chamada')),
                ('duration', models.TimeField(blank=True, null=True, verbose_name='Duração da Ligação')),
            ],
            options={
                'verbose_name': 'Conta',
                'ordering': ['-id'],
            },
        ),
    ]