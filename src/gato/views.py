from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from gato.models import Categoria, Gato, SolicitudAdopcion
from gato.forms import CategoriaForm, GatoForm, SolicitudAdopcionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoriaList(ListView):
    model = Categoria
    # template_name = "core/categoria_list.html"
    # queryset = Categoria.objects.all()
    # context_object_name = "categorias"

    def get_queryset(self): 
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = Categoria.objects.filter(nombre__contains=consulta) 
        else:
            queryset = Categoria.objects.all()
        return queryset


class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("gato:categoria_home")

class CategoriaUpdate(LoginRequiredMixin, UpdateView):  
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("gato:categoria_home")
    # template_name = "core/categoria_form.html"


class CategoriaDetail(DetailView):
    model = Categoria


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy("gato:categoria_home")


class GatoList(ListView):
    model = Gato

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = Gato.objects.filter(nombre__icontains=consulta)
        else:
            queryset = Gato.objects.all()
        return queryset


class GatoCreate(LoginRequiredMixin,CreateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("gato:gato_home")


class GatoUpdate(LoginRequiredMixin, UpdateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("gato:gato_home")


class GatoDetail(DetailView):
    model = Gato


class GatoDelete(LoginRequiredMixin, DeleteView):
    model = Gato
    success_url = reverse_lazy("gato:gato_home")


class SolicitudAdopcionList(ListView):
    model = SolicitudAdopcion
    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = SolicitudAdopcion.objects.filter(nombre__icontains=consulta)
        else:
            queryset = SolicitudAdopcion.objects.all()
        return queryset


class SolicitudAdopcionCreate(LoginRequiredMixin, CreateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    success_url = reverse_lazy("gato:solicitud_home")


class SolicitudAdopcionUpdate(LoginRequiredMixin, UpdateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    success_url = reverse_lazy("gato:solicitud_home")


class SolicitudAdopcionDetail(DetailView):
    model = SolicitudAdopcion


class SolicitudAdopcionDelete(LoginRequiredMixin,DeleteView):
    model = SolicitudAdopcion
    success_url = reverse_lazy("gato:solicitud_home")