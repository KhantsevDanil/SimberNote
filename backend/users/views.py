from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserChangeForm, CustomUserCreationForm


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("note:index")
    template_name = "signup.html"

class Login(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("note:index")
    template_name = "login.html"
