# Generated by Django 2.0.4 on 2018-05-17 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0012_auto_20180513_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='call_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calls.Call', verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='call',
            name='type',
            field=models.IntegerField(choices=[(1, 'start'), (2, 'end')], verbose_name='Tipo da ligação'),
        ),
    ]
