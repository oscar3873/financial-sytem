# Generated by Django 4.1.2 on 2023-02-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_adviser'),
        ('credit', '0004_alter_credit_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='client',
            field=models.ForeignKey(blank=True, default=None, help_text='Cliente del Credito', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_credits', to='clients.client'),
        ),
    ]
