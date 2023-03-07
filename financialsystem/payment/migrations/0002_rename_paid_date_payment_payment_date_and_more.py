# Generated by Django 4.1.7 on 2023-03-06 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_rename_refinancing_interest_refinancing_interest_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paid_date',
            new_name='payment_date',
        ),
        migrations.AddField(
            model_name='payment',
            name='installment_ref',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='credit.installmentrefinancing'),
        ),
    ]