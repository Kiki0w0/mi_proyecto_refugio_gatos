from django.contrib.auth.decorators import login_not_required  # type:ignore
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


@login_not_required
def home(request):
    return render(request, "core/index.html")


@method_decorator(login_not_required, name="dispatch")
class RegisterView(CreateView):
    template_name = "core/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:login")
