# Generated by Django 4.1.5 on 2023-04-05 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guarantor', '0003_guarantor_is_prueba_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guarantor',
            name='is_prueba',
        ),
        migrations.RemoveField(
            model_name='guarantor',
            name='is_prueba_1',
        ),
    ]
