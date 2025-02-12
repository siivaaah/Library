from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from app1.models import Menuitem,Menu


# class Home(ListView):
#     model=Menu
#     template_name="home.html"
#     context_object_name="menu"

def home(request):
    m=Menu.objects.all()
    context={'menu':m}
    return render(request,'home.html',context)

class Add(CreateView):
    model = Menuitem
    template_name = 'add.html'
    fields = ['name','price','menu','is_vegetarian']
    success_url = reverse_lazy('home')

class View(DetailView):
    model=Menu
    template_name="view.html"
    context_object_name="m"

class Update(UpdateView):
    model=Menuitem
    template_name='update.html'
    fields=['price']
    success_url=reverse_lazy('home')

class List(ListView):
    model=Menu
    template_name='list.html'
    context_object_name='m'


