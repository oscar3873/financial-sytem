# Generated by Django 4.1.7 on 2023-03-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_credit_mov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refinancing',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
