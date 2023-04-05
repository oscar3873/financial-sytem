from datetime import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from babel.dates import format_date
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse_lazy

#CRUD Guarantor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

from cashregister.utils import create_cashregister
from credit.models import Credit
from .models import Guarantor
from .forms import *
from .filters import ListingFilter

# Create your views here.
class GuarantorListView(LoginRequiredMixin, ListView):
    """
    Lista de clientes con autenticacion de logeo.
    """
    model = Guarantor
    template_name = 'guarantor/guarantor_list.html'
    ordering = ['-created_at']
    paginate_by = 8
    filter_class = ListingFilter
    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    
    def get_context_data(self, **kwargs):
        """
        Extrae los datos de los clientes que se encuentran en la base de datos para usarlo en el contexto.
        """
        create_cashregister()

        # Obtén los objetos clients filtrados
        guarantors = self.model.objects.all()
        filtered_guarantors = ListingFilter(self.request.GET, guarantors)
        
        # Pagina los objetos clients filtrados
        paginator = Paginator(filtered_guarantors.qs, self.paginate_by)
        page = self.request.GET.get('page')
        guarantors_paginated = paginator.get_page(page)
        print(guarantors_paginated.number, page)

        context = super().get_context_data(**kwargs)
        # Etiqueta para el día actual
        today = timezone.now().date()

        # Etiqueta para el mes actual
        month = datetime.today().month
        label_month = format_date(timezone.now(), format='MMMM Y', locale='es').capitalize()
        label_day = f'Hoy {timezone.now().date().day} de {label_month}'
        year = timezone.now().year
        label_year = str(year)
        label_historial = "Historico"
        # Cantidad de clientes histórica
        count_guarantors = self.model.objects.count()
        count_guarantors_today = self.model.objects.filter(created_at__date=today).count()
        count_guarantors_this_month = self.model.objects.filter(created_at__year=year, created_at__month=month).count()
        count_guarantors_this_year = self.model.objects.filter(created_at__year=year).count()
        count_guarantors_dict = [
            {'label':label_historial, 'value':count_guarantors},
            {'label':label_day, 'value':count_guarantors_today},
            {'label':label_month, 'value':count_guarantors_this_month},
            {'label':label_year, 'value':count_guarantors_this_year},
        ]
        
        # Contextos
        context["count_guarantors_dict"] = count_guarantors_dict
        context["guarantors"] = guarantors_paginated
        context["listing_filter"] = filtered_guarantors
        return context
    
    def get_queryset(self):
        """
        Retorna un queryset de objetos que serán utilizados para renderizar la vista.
        """
        queryset = super().get_queryset()
        self.filterset = self.filter_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.order_by(*self.ordering)

    def get_success_url(self) -> str:
        """
        Función que se encarga de devolver la URL de la vista actual.
        """
        return reverse_lazy('guarantors:list')

class GuarantorDetailView(LoginRequiredMixin, DetailView):
    """
    Detalle de un garante.
    """
    model = Guarantor
    template_name = "guarantor/guarantor_detail.html"
    
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    def get_object(self):
        """
        Retorna un objeto que será utilizado para renderizar la vista.
        """	
        return get_object_or_404(Guarantor, id=self.kwargs['pk'])

#CREACION DE UNA NOTA
def guarantorCreateView(request):
    guarantor_form = GuarantorForm(request.POST or None, prefix="guarantor")
    formsetPhoneGuarantor = PhoneNumberFormSetG(request.POST or None, instance=Guarantor(), prefix = "phone_number_guarantor")
    formsetPhoneGuarantor.extra = 4

    context = {
            'form': guarantor_form,
            'formsetPhoneG': formsetPhoneGuarantor,
        }
    
    if request.method == 'POST':
        if guarantor_form.is_valid() and formsetPhoneGuarantor.is_valid():
            guarantor = guarantor_form.save(commit=False)
            guarantor.adviser = request.user.adviser

            # Recuperar el ID del cliente seleccionado
            selected_client_id = request.POST.get('selected_client_id')

            try:
                credit = Credit.objects.get(pk=selected_client_id)
                guarantor.save()
                credit.guarantor = guarantor
                credit.save()
            except:
                messages.warning(request, 'El garante debe tener un credito asociado.',"warning")
                return render(request, 'guarantor/guarantor_form.html', context)

            phone_numbers = formsetPhoneGuarantor.save(commit=False)
            for phone_number in phone_numbers:
                if phone_number.phone_number_g:
                    phone_number.guarantor = guarantor
                    phone_number.save()
            messages.success(request, 'El garante se ha guardado exitosamente.',"success")
            return redirect('guarantors:list')

    return render(request, 'guarantor/guarantor_form.html', context)

#BORRADO DE UNA NOTA
#------------------------------------------------------------------
def delete_guarantor(request, pk):
    guarantor = get_object_or_404(Guarantor, pk=pk)
    guarantor.delete()
    messages.warning(request, 'Garante eliminado correctamente',"warning")
    return  redirect('guarantors:list')

#ACTUALIZACION DE UN MOVIMIENTO
#------------------------------------------------------------------
def update_guarantor(request, pk):
    """
    Actualiza un cliente y sus teléfonos.
    """
    guarantor = get_object_or_404(Guarantor, pk=pk)
    form = GuarantorForm(instance=guarantor)
    phone_formset = PhoneNumberFormSetG(instance=guarantor)
    phone_formset.extra = 4

    if request.method == 'POST':
        form = GuarantorForm(request.POST, instance=guarantor)  # Update the form variable with POST data
        phone_formset = PhoneNumberFormSetG(request.POST, instance=guarantor)
        if form.is_valid() and phone_formset.is_valid():
            client = form.save()

            phone_numbers = phone_formset.save(commit=False)
            for phone_number in phone_numbers:
                if phone_number.phone_number_c:
                    phone_number.guarantor = guarantor
                    phone_number.save()

            messages.success(request, 'Los datos del cliente se actualizaron correctamente.','success')
            return redirect('guarantors:list')

        else:
            print('ERROR: CLIENTE-TEL', form.errors, '-', phone_formset.errors)

    context = {
        'form': form,
        'phone_formset': phone_formset,
        'client': client,
    }

    return render(request, 'guarantor/guarantor_update.html', context)

