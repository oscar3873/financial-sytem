# Generated by Django 4.1.2 on 2023-03-09 20:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name', max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(help_text='Last name', max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(help_text='Email address', max_length=254, verbose_name='Correo electronico')),
                ('civil_status', models.CharField(blank=True, choices=[('S', 'Soltero'), ('C', 'Casado'), ('V', 'Viudo'), ('D', 'Divorciado')], max_length=10, verbose_name='Estado civil')),
                ('dni', models.PositiveIntegerField(help_text='dni number', verbose_name='DNI')),
                ('profession', models.CharField(help_text='Profession', max_length=50, verbose_name='Profesion')),
                ('address', models.CharField(help_text='Address', max_length=250, verbose_name='Direccion')),
                ('job_address', models.CharField(help_text='Job address', max_length=250, verbose_name='Direccion laboral')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('credit', models.ForeignKey(blank=True, default=None, help_text='Garantia del Credito', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_clients', to='credit.credit')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PhoneNumberGuarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_g', models.CharField(blank=True, help_text='Phone number', max_length=50, null=True, verbose_name='Numero de Telefono')),
                ('phone_type_g', models.CharField(choices=[('C', 'Celular'), ('F', 'Fijo'), ('A', 'Alternativo')], help_text='Type of phone', max_length=20, verbose_name='Tipo de Telefono')),
                ('guarantor', models.ForeignKey(blank=True, default='Some String', on_delete=django.db.models.deletion.CASCADE, to='guarantor.guarantor')),
            ],
        ),
    ]
