from django.forms import ModelForm
from .models import Contact



class ContacForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date', 'user',)
        labels = {
            'name': 'Nombre',
            'last:_name': 'Apellido',
            'mobile': 'CEL',
            'phone2': 'TEL',
            'company': 'Empresa',
            'date': 'Fecha',
            'notes': 'Nota'
        }

    

    
