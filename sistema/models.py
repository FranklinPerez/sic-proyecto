from django.db import models
from datetime import *
from django.utils import timezone

#modelo para los usuarios del sistema
class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (
		('s','Secretaria'),
		('m', 'Medico'),		
		)

	tipo_usuario= models.CharField(
        max_length=10,
        choices=TIPO_USUARIO,
        blank=True,
        default='sssssqqqqq',
        help_text='Tipo de usuario en el sistema')

	def __str__(self):
		 return '{0}, {1},{2}'.format(self.codUsu, self.pasUsu, self.tipo_usuario)
#fin modelo para los usuarios del sistema

#modelos para los usuarios del sistema
class Secretaria(models.Model):
	codigoSec=models.IntegerField(help_text="Ingrese el codigo de la Secretaria",primary_key = True)
	nombreSec=models.CharField(max_length=200,help_text="Ingrese el nombre de la Secretaria")
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nomSec
#fin modelos para los usuarios del sistema

#modelos para las cuentas
class Cuenta(models.Model):
	codigoCuenta=models.CharField(max_length=20,help_text="codigo de la cuenta")
	nombreCuenta=models.IntegerField(help_text="Ingrese el codigo de la Secretaria",primary_key = True)
	tipoCuenta=models.CharField(max_length=200,help_text="nombre de la cuenta")
	saldo=models.IntegerField(help_text="saldo de la cuenta")
	TIPO_CUENTA= (
		('pasivo','pasivo'),
		('activo', 'activo'),
		('capital', 'capital'),
		('inventario', 'inventario'),
		('resultados', 'resultados'),
		('ingresos', 'ingresos'),		
		)

	tipo_usuario= models.CharField(
        max_length=30,
        choices=TIPO_CUENTA,
        blank=True,
        default='activo',
        help_text='Tipo de cuenta contable')
	def __str__(self):
		return self.nomSec

class SubCuenta(Cuenta):
	def __str__(self):
		return self.nomSec

#fin modelos para las cuentas