from django.shortcuts import render, redirect, get_object_or_404
from .models import Temat, Notatka
from .forms import TematForm, NotatkaForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def lista_tematow(request):
    zapytanie = request.GET.get('szukaj', '')
    tematy = Temat.objects.filter(uzytkownik=request.user)
    if zapytanie:
        tematy = tematy.filter(nazwa__icontains=zapytanie)
    return render(request, 'nauka/lista.html', {'tematy': tematy, 'szukaj': zapytanie})

@login_required
def dodaj_temat(request):
    if request.method == 'POST':
        form = TematForm(request.POST)
        if form.is_valid():
            temat = form.save(commit=False)
            temat.uzytkownik = request.user
            temat.save()
            return redirect('lista')
    else:
        form = TematForm()
    return render(request, 'nauka/formularz.html', {'form': form, 'typ': 'Temat'})

@login_required
def szczegoly_temat(request, temat_id):
    temat = get_object_or_404(Temat, id=temat_id, uzytkownik=request.user)
    notatki = Notatka.objects.filter(temat=temat)
    return render(request, 'nauka/szczegoly.html', {'temat': temat, 'notatki': notatki})

@login_required
def dodaj_notatke(request, temat_id):
    temat = get_object_or_404(Temat, id=temat_id, uzytkownik=request.user)
    if request.method == 'POST':
        form = NotatkaForm(request.POST)
        if form.is_valid():
            notatka = form.save(commit=False)
            notatka.temat = temat
            notatka.save()
            return redirect('szczegoly', temat_id=temat.id)
    else:
        form = NotatkaForm()
    return render(request, 'nauka/formularz.html', {'form': form, 'typ': 'Notatka'})

class EdytujTemat(LoginRequiredMixin, UpdateView):
    model = Temat
    fields = ['nazwa', 'poziom', 'osiagniecia']
    template_name = 'nauka/formularz.html'
    success_url = reverse_lazy('lista')

    def get_queryset(self):
        return Temat.objects.filter(uzytkownik=self.request.user)

class UsunTemat(LoginRequiredMixin, DeleteView):
    model = Temat
    template_name = 'nauka/potwierdzenie_usuniecia.html'
    success_url = reverse_lazy('lista')

    def get_queryset(self):
        return Temat.objects.filter(uzytkownik=self.request.user)
