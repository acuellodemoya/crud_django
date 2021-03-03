from django.shortcuts import render, redirect
from .models import User
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

class UserCreate(CreateView):
    
    model = User
    form_class = UserForm
    template_name = 'crear.html'
    success_url = reverse_lazy('index')

class UserList(ListView):
    model = User
    template_name = 'listar.html'

class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'crear.html'
    success_url = reverse_lazy('listar_usuarios')