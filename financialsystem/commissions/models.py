from datetime import datetime
from django.db import models

from cashregister.models import Movement
from adviser.models import Adviser

from django.db.models.signals import pre_save, post_delete

from core.utils import round_to_nearest_hundred


# Create your models here.
###############################################################################

class Commission(models.Model):
    MONEY_TYPE = [
        ('PESOS','PESOS'),
        ('USD','USD'),
        ('EUR', 'EUR'),
        ('TRANSFER','TRANSFERENCIA'),
        ]
    
    REG = [
        ('REGISTRO','REGISTRO'),
        ('COBRO','COBRO'),
        ('VENTA', 'VENTA')
        ]

    is_paid = models.BooleanField(default=False)

    adviser = models.ForeignKey(Adviser,on_delete=models.SET_NULL,null=True)
    interest = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    amount = models.DecimalField(blank=False, decimal_places=2, max_digits=20)
    operation_amount = models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True) 
    type = models.CharField(max_length=20, null=True,choices=REG)
    money_type = models.CharField(max_length=20 , null=True, choices=MONEY_TYPE, default= 'PESOS')
    last_up = models.DateTimeField(default=datetime.now)
    mov = models.OneToOneField(Movement, on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField(max_length=100, null=True, blank=True, help_text="Detalle de la operacion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Interest(models.Model):
    """
    Clase para podes asignar de manera uniboca los intereses por comisiones y puntajes para clientes
    """
    interest_credit = models.DecimalField(max_digits=5, decimal_places=2, default=40, help_text="Interes general para creditos")
    interest_register = models.DecimalField(max_digits=5, decimal_places=2, default=7.5 , help_text="Comision por registro")
    interest_payment = models.DecimalField(max_digits=5, decimal_places=2, default=5, help_text="Comision por cobro")
    interest_sell = models.DecimalField(max_digits=5, decimal_places=2, default=2 , help_text="Comision por venta")
    points_score_refinancing = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=80 , help_text="Puntos por refinanciacion pagada")
    points_score_credits = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=100 , help_text="Puntos por credito pagado")
    daily_interest = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=5 , help_text="Disminucion de puntos por retraso diario")
    porcentage_daily_interest = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=2 , help_text="Porcentaje de interes por retraso diario")


#-------------------------- SEÑALES PARA COMMISSION --------------------------------------
def paid_commission(instance, *args, **kwargs):
    '''Actualiza la comisión de una instancia si ha sido pagada. 
    Calcula el valor real de la comisión basado en la última tasa de interés almacenada. 
    Actualiza el monto y la tasa de interés de la instancia, y el tiempo de última actualización.'''
    instance.amount = round_to_nearest_hundred(instance.amount)
    match(instance.type):
        case 'REGISTRO': instance.interest = Interest.objects.first().interest_register
        case 'COBRO': instance.interest = Interest.objects.first().interest_payment
        case _ : instance.interest = Interest.objects.first().interest_sell
            

def delete_commission_mov(instance, *args, **kwargs):
    '''
    Eliminacion 'bidireccional': Elimina la instancia de la comision y el moviminto realizado.
    '''
    try:
        if instance.mov:
            instance.mov.delete()
    except: pass

pre_save.connect(paid_commission, sender=Commission)
post_delete.connect(delete_commission_mov, sender=Commission)