from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from config.settings import AUTH_USER_MODEL
from django.shortcuts import render
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def auth_view(request):
    return render(request, 'home.html', {'auth': AUTH_USER_MODEL})