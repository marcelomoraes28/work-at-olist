# Generated by Django 2.0.4 on 2018-05-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('connection_cost', models.FloatField(verbose_name='Valor por ligação')),
                ('cost_per_minute', models.FloatField(verbose_name='Valor por minuto')),
                ('initial_period', models.TimeField(verbose_name='Início do período comercial')),
                ('end_period', models.TimeField(verbose_name='Final do período comercial')),
                ('status', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo')], verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Configuração dos custos',
                'ordering': ['-id'],
            },
        ),
    ]
