# Generated by Django 4.1.2 on 2023-02-24 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adviser', '0005_rename_c_type_comission_type_comission_checked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comission',
            name='adviser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
