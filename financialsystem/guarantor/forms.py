from django import forms
from django.core.validators import validate_email
from django.forms import inlineformset_factory
from guarantor.models import Guarantor, PhoneNumberGuarantor

#FORMULARIO PARA LA CREACION DEL CLIENTE
#------------------------------------------------------------------
class GuarantorForm(forms.ModelForm):
    
    prefix = 'guarantor'
    
    CIVIL_STATUS = (
        ('S','Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado')
    )
    
    first_name = forms.CharField(
        label = 'Nombre/s',
    )
    
    last_name = forms.CharField(
        label = 'Apellido/s',
    )
    
    email = forms.EmailField(
        label= 'Correo Electrónico',
    )
    
    civil_status = forms.ChoiceField(
        choices= CIVIL_STATUS,
        label= "Estado Civil"
    )
    
    dni = forms.IntegerField(
        label= "DNI",
    )
    
    profession = forms.CharField(
        label= "Profesion",
    )
    
    address = forms.CharField(
        label= "Domicilio",
    )
    
    job_address = forms.CharField(
        label= "Domicilio Laboral",
    )
    
    class Meta:
        model = Guarantor
        fields = "__all__"
        exclude = ["credit"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'class': 'form-control'})
        
        # Eliminar validación requerida
        for field in self.fields.values():
            field.required = False    
        
#FORMULARIO PARA UPDATES
#-----------------------------------------------------------------
class GuarantorUpdateForm(forms.ModelForm):
    
    prefix = 'guarantor'
    
    CIVIL_STATUS = (
        ('S','Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado')
    )
    
    first_name = forms.CharField(
        label = 'Nombre/s',
        required=True,
    )
    last_name = forms.CharField(
        label = 'Apellido/s',
        required=True,
    )
    email = forms.EmailField(
        label= 'Correo',
        required=True,
    )
    civil_status = forms.ChoiceField(
        label="Estado Civil",
        choices= CIVIL_STATUS,
        required=True,
    )
    dni = forms.IntegerField(
        label= "DNI",
        required=True,
    )
    profession = forms.CharField(
        label= "Profesion",
        required=True,
    )
    address = forms.CharField(
        label= "Domicilio",
        required=True,
    )
    job_address = forms.CharField(
        label= "Domicilio Laboral",
        required=True,
    )
    
    class Meta:
        model = Guarantor
        fields = "__all__"
        exclude = ["credit"]

    def clean(self):
        """
        Validar que todos los campos estén requeridos
        """	
        cleaned_data = super().clean()
        fields_to_validate = ['first_name', 'last_name', 'address', 'job_address']
        
        for field_name in fields_to_validate:
            field_value = cleaned_data.get(field_name)
            if not field_value:
                self.add_error(field_name, 'Este campo es requerido')
                
        return cleaned_data
    
    def clean_dni(self):
        """
        Validar que el DNI sea válido
        """
        dni = self.cleaned_data.get('dni')
        if len(str(dni)) < 7 or  len(str(dni)) >= 15:
            raise forms.ValidationError("El DNI debe contener como mínimo 7 y máximo 15 caracteres")

        try:
            existing_guarantor = Guarantor.objects.get(dni=dni)
            if self.instance.pk != existing_guarantor.pk:
                raise forms.ValidationError("Ya existe un Cliente con DNI: %s" % dni )
        except Guarantor.DoesNotExist:
            pass

        return dni

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError("El nombre debe contener al menos 3 caracteres")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError("El apellido debe contener al menos 3 caracteres")
        return last_name

    def clean_email(self):
        """
        Validar que el correo electrónico sea válido
        """
        email = self.cleaned_data.get('email')

        # Validar formato de correo electrónico
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Ingrese un correo electrónico válido")

        try:
            existing_guarantor = Guarantor.objects.get(email=email)
            if self.instance.pk != existing_guarantor.pk:
                raise forms.ValidationError("El correo: %s ya esta en uso" % email)
        except Guarantor.DoesNotExist:
            pass

        return email


    def __init__(self, *args, **kwargs):
        super(GuarantorUpdateForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'class': 'form-control'})

#FORMULARIO PARA LA CREACION DE LOS NUMEROS DE TELEFONO
#------------------------------------------------------------------
class PhoneNumberFormGuarantor(forms.ModelForm):
    
    PhoneType = (
        ('C', 'Celular'), 
        ('F', 'Fijo'),
        ('A', 'Alternativo')
    )
    
    phone_number_g = forms.CharField(
        label = 'Telefono',
    )
    
    phone_type_g = forms.ChoiceField(
        choices= PhoneType,
        label="Tipo"
    )
    
    class Meta:
        model = PhoneNumberGuarantor
        fields = ('phone_number_g', 'phone_type_g')
    
    def clean_phone_number_g(self):
        """
        Validacion de numero de telefono.
        """
        phone_number_g = self.cleaned_data.get('phone_number_g')
        if phone_number_g is None or phone_number_g == '':
            return None
        elif not phone_number_g.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos")
        elif len(phone_number_g) < 8 or len(phone_number_g) > 15:
            raise forms.ValidationError("El numero debe contener como minimo 8 y 15 digitos")
        return phone_number_g    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'class': 'form-control'})
        # Eliminar validación requerida
        for field in self.fields.values():
            field.required = False                

#------------------------------------------------------------------
PhoneNumberFormSetG = inlineformset_factory(
    Guarantor, 
    PhoneNumberGuarantor, 
    form = PhoneNumberFormGuarantor,
    extra= 2,
    can_delete= False,
)