from django.shortcuts import render, redirect
from .forms import CadastroMedico, CadastroEspecialidade
from .models import ESPECIALIDADE, MEDICO
from django.views.generic import ListView

# Create your views here.
def TelaCadastroMedico(request):
    if request.method == "POST":
        form = CadastroMedico(request.POST)
        print("\n\n\n\n\n\nForm recebido")
        #form.data['id_especialidade'] = ESPECIALIDADE.objects.get(pk=int(form.data['id_especialidade']))
        print(f'{form.data}\n\n\n\n\n')
        if form.is_valid():
            print("\n\n\n\n\n\n\n\n\n\nVALIDO\n\n\n\n\n\n\n\n")
            form.save()
            medico_criado=MEDICO.objects.all().last()
            medico_criado.id_especialidade=ESPECIALIDADE.objects.get(pk=form.data['id_especialidade'])
            medico_criado.save()
            return redirect('cadastro_medico')
        else:
            print("\n\n\n\n\n\n\n\n\nNAO VALIDO D JLSHADJKLSHAJKLDHASKDJSA\n\n\n\n\n\n\n\n")
    else:
        form = CadastroMedico()
    return render(request, 'medico/cadastro_medico.html', {'form': form})

def TelaCadastroEspecialidade(request):
    if request.method == "POST":
        form = CadastroEspecialidade(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_especialidade')
    else:
        form = CadastroEspecialidade()
    return render(request, 'medico/cadastro_especialidade.html', {'form': form})

class ListarMedicos(ListView):
    model = MEDICO
    context_object_name = 'medicos'
    template_name = 'medico/medicos.html'

    def get_queryset(self):
        return MEDICO.objects.all()
    
class ListarEspecialidades(ListView):
    model = ESPECIALIDADE
    context_object_name = 'especialidades'
    template_name = 'medico/especialidades.html'

    def get_queryset(self):
        return ESPECIALIDADE.objects.all()
    