from django.contrib import admin
from .models import Credit, Installment, Refinancing, InstallmentRefinancing

# Register your models here.
class CreditAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'guarantor',
        'has_pay_stub',
        'amount',
        'installment_num', 
        'interest',
        'credit_repayment_amount', 
        'is_paid',
        'created_at', 
        'updated_at'
    )

class InstallmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'credit',
        'installment_number', 
        'amount', 
        'is_caduced_installment', 
        'is_paid_installment',
        'refinance',
        'is_refinancing_installment', 
        'created_at', 
        'updated_at'
    )

class RefinancingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_paid',
        'interest', 
        'amount', 
        'refinancing_repayment_amount', 
        'installment_num',
        'created_at',
        'updated_at'
    )
    
    
class InstallmentRefinancingAdmin(admin.ModelAdmin):
    list_display = (
        'credit',
        'id',
        'refinancing',
        'installment_number',
        'daily_interests',
        'amount', 
        'payment_date', 
        'is_caduced_installment', 
        'is_paid_installment', 
        'lastup',
        'created_at', 
        'updated_at'
    )

admin.site.register(Credit, CreditAdmin)
admin.site.register(Installment, InstallmentAdmin)
admin.site.register(Refinancing, RefinancingAdmin)
admin.site.register(InstallmentRefinancing, InstallmentRefinancingAdmin)