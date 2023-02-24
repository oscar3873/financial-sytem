# Generated by Django 4.1.7 on 2023-02-23 01:06

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cashregister', '0002_alter_cashregister_total_balancears_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashregister',
            name='total_balanceARS',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='ARS', max_digits=20, null=True),
        ),
    ]