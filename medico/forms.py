from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MEDICO, ESPECIALIDADE

lista = []
opcoes = ESPECIALIDADE.objects.values('id_especialidade', 'nome')

for opcao in opcoes:
    novo = []
    for k,v in opcao.items():
        novo.append(v)
    if len(novo) == 2:
        lista.append((novo[0], novo[1]))

class CadastroMedico(forms.ModelForm):
    id_especialidade = forms.ChoiceField(choices=lista, widget=forms.Select())

    class Meta:
        model = MEDICO
        fields = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm']

class CadastroEspecialidade(forms.ModelForm):

    class Meta:
        model = ESPECIALIDADE
        fields = ['nome', 'descricao']