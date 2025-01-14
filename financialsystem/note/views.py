from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy

#CRUD Note
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from cashregister.utils import create_cashregister
from .models import Note
from .forms import NoteForm

# Create your views here.
class NoteListView(LoginRequiredMixin, ListView):
    """
    Lista de notas.
    """
    model = Note
    template_name = "note/note_list.html"
    paginate_by = 6
    ordering = ['-created_at']

    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        """
        Extrae los datos de las notas que se encuentran en la base de datos para usarlo en el contexto.
        """
        create_cashregister()
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["count_notes"] = self.model.objects.all().count()
        context["notes"] = self.model.objects.all()
        #VALIDACION DE EXISTENCIA PARA AL MENOS UN CLIENTE
        if self.model.objects.all().count() > 0:
            context["properties"] = self.model.objects.all()[0].all_properties()
        
        return context

class NoteDetailView(LoginRequiredMixin, DetailView):
    """
    Detalle de las notas.
    """
    model = Note
    template_name = "note/note_detail.html"
    
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    
    def get_object(self):
        """
        Retorna un objeto que será utilizado para renderizar la vista.
        """	
        return get_object_or_404(Note, id=self.kwargs['pk'])

#CREACION DE UNA NOTA
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'
          
    def form_valid(self, form):
        if form.is_valid():
            note = form.save(commit=False)
            print('si pasa')

            note.color = "yellow" if self.request.user.is_superuser else "blue"
            note.user = self.request.user.adviser
            form.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        """
        Función que se encarga de obtener los parámetros del formulario.
        """
        kwargs = super(NoteCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def get_success_url(self) -> str:
        """
        Redirecciona al listado de notas, con un mensaje de creacion exitosa.
        """
        messages.success(self.request, 'Nota creada correctamente', "success")
        return  reverse_lazy('notes:list')

#BORRADO DE UNA NOTA
#------------------------------------------------------------------
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    """
    Borrar una nota.
    """
    model = Note

    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    
    def get_success_url(self) -> str:
        """
        Redirecciona al listado de notas, con un mensaje de creacion exitosa.
        """
        messages.warning(self.request, 'Nota eliminada correctamente', "warning")
        return  reverse_lazy('notes:list')

#ACTUALIZACION DE UN MOVIMIENTO
#------------------------------------------------------------------
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name_suffix = '_update_form'

    #CARACTERISTICAS DEL LOGINREQUIREDMIXIN
    login_url = "/accounts/login/"
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """
        Función que se encarga de obtener los parámetros del formulario.
        """
        kwargs = super(NoteUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def get_success_url(self) -> str:
        """
        Redirecciona al listado de notas, con un mensaje de creacion exitosa.
        """
        messages.info(self.request, 'Nota actualizada satisfactoriamente', "info")
        return  reverse_lazy('notes:list')