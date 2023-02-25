# Generated by Django 4.1.5 on 2023-02-25 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("credit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_refinancing_pay", models.BooleanField(default=False)),
                (
                    "detaill",
                    models.CharField(
                        blank=True, help_text="Detalle del pago", max_length=250
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "installment",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        help_text="Cuota que se esta pagando",
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="installment_pay",
                        to="credit.installment",
                    ),
                ),
                (
                    "refinancing",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        help_text="Refinanciacion que se esta pagando",
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="refinancing_pay",
                        to="credit.installmentrefinancing",
                    ),
                ),
            ],
        ),
    ]
