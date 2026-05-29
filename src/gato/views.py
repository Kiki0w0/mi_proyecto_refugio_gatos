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


class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("gato:categoria_home")

class CategoriaUpdate(UpdateView):  
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("gato:categoria_home")
    # template_name = "core/categoria_form.html"


class CategoriaDetail(DetailView):
    model = Categoria


class CategoriaDelete(DeleteView):
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


class GatoCreate(CreateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("gato:gato_home")


class GatoUpdate(UpdateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("gato:gato_home")


class GatoDetail(DetailView):
    model = Gato


class GatoDelete(DeleteView):
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


class SolicitudAdopcionCreate(CreateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    success_url = reverse_lazy("gato:solicitud_home")


class SolicitudAdopcionUpdate(UpdateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    success_url = reverse_lazy("gato:solicitud_home")


class SolicitudAdopcionDetail(DetailView):
    model = SolicitudAdopcion


class SolicitudAdopcionDelete(DeleteView):
    model = SolicitudAdopcion
    success_url = reverse_lazy("gato:solicitud_home")