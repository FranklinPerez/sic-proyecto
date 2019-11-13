# Generated by Django 2.2.7 on 2019-11-12 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('codigoCuenta', models.CharField(help_text='codigo de la cuenta', max_length=20)),
                ('nombreCuenta', models.IntegerField(help_text='Ingrese el codigo de la Secretaria', primary_key=True, serialize=False)),
                ('tipoCuenta', models.CharField(help_text='nombre de la cuenta', max_length=200)),
                ('saldo', models.IntegerField(help_text='saldo de la cuenta')),
                ('tipo_usuario', models.CharField(blank=True, choices=[('pasivo', 'pasivo'), ('activo', 'activo'), ('capital', 'capital'), ('inventario', 'inventario'), ('resultados', 'resultados'), ('ingresos', 'ingresos')], default='activo', help_text='Tipo de cuenta contable', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codUsu', models.CharField(help_text='Ingrese el Usuario, maximo 10 caracteres', max_length=10, primary_key=True, serialize=False)),
                ('pasUsu', models.CharField(help_text='Ingrese contraseña, maximo 20 caracteres', max_length=20)),
                ('tipo_usuario', models.CharField(blank=True, choices=[('s', 'Secretaria'), ('m', 'Medico')], default='sssssqqqqq', help_text='Tipo de usuario en el sistema', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubCuenta',
            fields=[
                ('cuenta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sistema.Cuenta')),
            ],
            bases=('sistema.cuenta',),
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('codigoSec', models.IntegerField(help_text='Ingrese el codigo de la Secretaria', primary_key=True, serialize=False)),
                ('nombreSec', models.CharField(help_text='Ingrese el nombre de la Secretaria', max_length=200)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.Usuario')),
            ],
        ),
    ]