# Generated by Django 4.1.5 on 2023-03-30 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_credit_guarantor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='guarantor',
        ),
    ]
