from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from angajat.models import Angajat


# Create your views here.
class AngajatView(LoginRequiredMixin, ListView):
    model = Angajat
    template_name = 'angajat/angajat_index.html'


class CreateAngajatView(LoginRequiredMixin, CreateView):
    model = Angajat
    fields = ['nume', 'prenume', 'varsta', 'domeniu', 'salariu']
    template_name = 'angajat/angajat_form.html'

    def get_success_url(self):
        return reverse('angajat:lista_angajat')


class UpdateAngajatView(LoginRequiredMixin, UpdateView):
    model = Angajat
    fields = ['nume', 'prenume', 'varsta', 'domeniu', 'salariu']
    template_name = 'angajat/angajat_form.html'

    def get_success_url(self):
        return reverse('angajat:lista_angajat')


@login_required
def delete_angajat(request, pk):
    Angajat.objects.filter(id=pk).update(active=0)
    return redirect('angajat:lista_angajat')


@login_required
def activare_angajat(request, pk):
    Angajat.objects.filter(id=pk).update(active=1)
    return redirect('angajat:lista_angajat')
