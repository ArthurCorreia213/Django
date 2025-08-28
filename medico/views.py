from django.shortcuts import render, redirect
from .forms import CadastroMedico, CadastroEspecialidade

# Create your views here.
def TelaCadastroMedico(request):
    if request.method == "POST":
        form = CadastroMedico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_medico')
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