# Generated by Django 4.1.7 on 2023-03-06 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['created_at']},
        ),
    ]
