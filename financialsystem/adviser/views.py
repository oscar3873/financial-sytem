from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from braces.views import GroupRequiredMixin

from credit.utils import refresh_condition
from .models import Adviser, Comission
from .utils import commission_properties
from .forms import PorcentageUpdate
from cashregister.models import CashRegister, Movement

# Create your views here.
class AdviserListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Adviser
    group_required = "admin_group"
    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'
    
    def handle_no_permission(self):
        return redirect("/accounts/login/")
    
    def get_context_data(self, **kwargs):
        refresh_condition()
        context = super().get_context_data(**kwargs)
        context["count_advisers"] = Adviser.objects.count()
        context["advisers"] = Adviser.objects.all()
        return context
    

class AdviserDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Adviser
    
    group_required = "admin_group"
    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'
    
    def handle_no_permission(self):
        return redirect("/")
    
    def get_context_data(self, **kwargs):
        refresh_condition()
        context = super().get_context_data(**kwargs)
        context["commissions"] = Comission.objects.filter(adviser=self.get_object(), is_paid=False)
        context["properties"] = commission_properties()
        return context

    def get_object(self):
        return get_object_or_404(Adviser, id=self.kwargs['pk'])

#----------------------------------------------------------------
@login_required(login_url="/accounts/login/")
def pay_commission(request, pk):
    refresh_condition()
    try:
        commission = Comission.objects.get(id=pk)
    except Comission.DoesNotExist:
        return redirect('advisers:detail', pk=commission.adviser.id)

    if commission.is_paid:
        messages.error(request, "Esta comisión ya ha sido pagada.")
        return redirect('advisers:detail', pk=commission.adviser.id)

    commission.is_paid = True
    porcentage = request.POST.get('porcentage')
    commission._last_interest = Decimal(porcentage)
    commission.save()
    create_movement(commission)

    messages.success(request, "La comisión se ha pagado exitosamente.")
    return redirect('advisers:detail', pk=commission.adviser.id)


class AdviserUpdateView(UpdateView):
    model = Adviser
    

class AdviserDeleteView(DeleteView):
    pass


def create_movement(commission):
    Movement.objects.create(
            user = commission.adviser,
            amount = commission.amount,
            cashregister = CashRegister.objects.last(),
            operation_mode = 'EGRESO',
            description = 'COMISION %s - %s' % (commission.adviser, commission.type),
            money_type= commission.money_type
        )