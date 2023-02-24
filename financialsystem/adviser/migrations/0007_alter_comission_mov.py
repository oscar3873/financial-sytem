# Generated by Django 4.1.2 on 2023-02-24 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashregister', '0005_alter_movement_user'),
        ('adviser', '0006_alter_comission_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comission',
            name='mov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cashregister.movement'),
        ),
    ]