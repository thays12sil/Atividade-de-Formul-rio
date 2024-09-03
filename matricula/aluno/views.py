from django.shortcuts import render, redirect
from .models import Estudante
from .forms import EstudanteForm
from django import forms  
def adicionar_estudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exibir_estudantes')
    else:
        form = EstudanteForm()
    return render(request, 'adicionar_estudante.html', {'form': form})

def exibir_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'exibir_estudantes.html', {'estudantes': estudantes})
