# Generated by Django 4.1.7 on 2023-03-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_rename_is_paid_credit_credit_is_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='condition',
            field=models.CharField(choices=[('Pagado', 'Pagado'), ('A Tiempo', 'A Tiempo')], default='A Tiempo', max_length=15),
        ),
        migrations.AlterField(
            model_name='installment',
            name='payment_date',
            field=models.DateTimeField(blank=True, help_text='Fecha de Pago', null=True),
        ),
        migrations.AlterField(
            model_name='installmentrefinancing',
            name='condition',
            field=models.CharField(choices=[('Pagada', 'Pagada'), ('A Tiempo', 'A Tiempo')], default='A Tiempo', max_length=15),
        ),
        migrations.AlterField(
            model_name='refinancing',
            name='payment_date',
            field=models.DateTimeField(blank=True, help_text='Fecha de Pago', null=True),
        ),
    ]