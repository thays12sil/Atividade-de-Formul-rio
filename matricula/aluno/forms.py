from django import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome_completo', 'endereco_residencial', 'cidade_moradia', 'email_pessoal', 'nome_curso']
