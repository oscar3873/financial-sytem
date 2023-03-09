# Generated by Django 4.1.7 on 2023-03-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0007_alter_sell_commission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warranty',
            name='is_selled',
        ),
        migrations.AlterField(
            model_name='warranty',
            name='state',
            field=models.CharField(blank=True, choices=[('NUEVO', 'NUEVO'), ('USADO:COMO NUEVO', 'USADO:COMO NUEVO'), ('USADO:MUY BUENO', 'USADO:MUY BUENO'), ('USADO:BUENO', 'USADO:BUENO'), ('USADO:ACEPTABLE', 'USADO:ACEPTABLE'), ('USADO:REACONDICIONADO', 'USADO:REACONDICIONADO'), ('USADO:MUCHO USO', 'USADO:MUCHO USO'), ('VENDIDO', 'VENDIDO')], max_length=30, verbose_name='Estado'),
        ),
    ]
