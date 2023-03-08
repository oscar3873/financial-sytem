# Generated by Django 4.1.2 on 2023-03-08 00:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('cashregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('is_active', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False, help_text='El credito esta pagado')),
                ('is_old_credit', models.BooleanField(default=False, help_text='Es un credito antiguo')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('condition', models.CharField(choices=[('Pagado', 'Pagado'), ('A Tiempo', 'A Tiempo')], default='A Tiempo', max_length=15)),
                ('credit_interest', models.PositiveIntegerField(default=40, help_text='Intereses de credito')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Monto del Credito', max_digits=15)),
                ('credit_repayment_amount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Monto de Devolucion del Credito', max_digits=15)),
                ('installment_num', models.PositiveIntegerField(default=1, help_text='Numeros de Cuotas', null=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Fecha de Finalizacion del Credito')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Pago')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, default=None, help_text='Cliente del Credito', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_credits', to='clients.client')),
                ('mov', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashregister.movement')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Refinancing',
            fields=[
                ('is_paid', models.BooleanField(default=False, help_text='La refinanciacion esta pagada')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('interest', models.PositiveIntegerField(default=48, help_text='Intereses de la refinanciacion')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('refinancing_repayment_amount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Monto de Devolver de la Refinanciacion', max_digits=15)),
                ('installment_num_refinancing', models.PositiveIntegerField(default=1, help_text='Numeros de Cuotas', null=True)),
                ('payment_date', models.DateTimeField(blank=True, help_text='Fecha de Pago', null=True)),
                ('lastup', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='InstallmentRefinancing',
            fields=[
                ('is_caduced_installment', models.BooleanField(default=False, help_text='La cuota esta vencida')),
                ('is_paid_installment', models.BooleanField(default=False, help_text='La cuota esta pagada')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('condition', models.CharField(choices=[('Pagada', 'Pagada'), ('A Tiempo', 'A Tiempo')], default='A Tiempo', max_length=15)),
                ('installment_number', models.PositiveSmallIntegerField(help_text='Numero de cuota de la refinanciacion')),
                ('daily_interests', models.DecimalField(decimal_places=2, default=0, help_text='Intereses diarios', max_digits=20, null=True)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Monto de la cuota de refinanciacion', max_digits=15)),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Pago')),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Vencimiento')),
                ('lastup', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('refinancing', models.ForeignKey(help_text='Refinanciacion de la cuota', on_delete=django.db.models.deletion.CASCADE, related_name='installments', to='credit.refinancing')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('is_caduced_installment', models.BooleanField(default=False, help_text='La cuota esta vencida')),
                ('is_paid_installment', models.BooleanField(default=False, help_text='La cuota esta pagada')),
                ('is_refinancing_installment', models.BooleanField(default=False, help_text='La cuota fue refinanciada')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('installment_number', models.PositiveSmallIntegerField(help_text='Numero de cuota del credito')),
                ('daily_interests', models.DecimalField(decimal_places=2, default=0, help_text='Intereses diarios', max_digits=20, null=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('payment_date', models.DateTimeField(blank=True, help_text='Fecha de Pago', null=True)),
                ('condition', models.CharField(choices=[('Pagada', 'Pagada'), ('Refinanciada', 'Refinanciada'), ('Vencida', 'Vencida'), ('A Tiempo', 'A Tiempo')], default='A Tiempo', max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Monto de la cuota', max_digits=15)),
                ('lastup', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('credit', models.ForeignKey(help_text='Credito de la cuota', on_delete=django.db.models.deletion.CASCADE, related_name='installments', to='credit.credit')),
                ('refinance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='installment_ref', to='credit.refinancing')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
