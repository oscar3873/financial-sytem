# Generated by Django 4.1.2 on 2023-02-28 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adviser', '0003_alter_comission_adviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comission',
            name='mov',
        ),
    ]