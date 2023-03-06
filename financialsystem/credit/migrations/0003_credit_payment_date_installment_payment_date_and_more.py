# Generated by Django 4.1.7 on 2023-03-04 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_remove_refinancing_mov'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Fecha de Pago'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installment',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Fecha de Pago'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refinancing',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Fecha de Pago'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='installmentrefinancing',
            name='condition',
            field=models.CharField(choices=[('Pagada', 'Pagada'), ('A Tiempo', 'A Tiempo'), ('Legales', 'Legales')], default='A Tiempo', max_length=15),
        ),
        migrations.AlterField(
            model_name='installmentrefinancing',
            name='payment_date',
            field=models.DateTimeField(help_text='Fecha de pago de la cuota de refinanciacion'),
        ),
    ]