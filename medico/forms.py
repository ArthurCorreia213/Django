from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MEDICO, ESPECIALIDADE


class CadastroMedico(forms.ModelForm):

    class Meta:
        model = MEDICO
        fields = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm']

class CadastroEspecialidade(forms.ModelForm):

    class Meta:
        model = ESPECIALIDADE
        fields = ['nome', 'descricao']