# Generated by Django 4.1.7 on 2023-03-08 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adviser', '0001_initial'),
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_refinancing_pay', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='Monto de Pago', max_digits=15)),
                ('payment_date', models.DateTimeField(default=datetime.datetime.now, help_text='Fecha de Pago')),
                ('payment_method', models.CharField(choices=[('PESOS', 'PESOS'), ('USD', 'USD'), ('EUR', 'EUR'), ('TRANSFER', 'TRANSFER'), ('CREDITO', 'CREDITO'), ('DEBITO', 'DEBITO')], help_text='Metodo de Pago', max_length=20)),
                ('detail', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adviser.adviser')),
                ('installment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='credit.installment')),
                ('installment_ref', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='credit.installmentrefinancing')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
