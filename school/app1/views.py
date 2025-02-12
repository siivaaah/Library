from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.management.commands.changepassword import UserModel
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView, DetailView

from app1.models import Student

from app1.forms import Registerform


class Home(TemplateView):
    # model=Student
    template_name="home.html"
    # context_object_name="student"


from app1.models import School
from django.urls import reverse_lazy
from app1.forms import Schoolform

class Addschool(CreateView):
    model=School
    # fields=['name','location','principle']
    form_class=Schoolform
    template_name="addschool.html"
    success_url=reverse_lazy('home')


class Addstudent(CreateView):
    model=Student
    fields=['name','age','school']
    template_name="addstudent.html"
    success_url=reverse_lazy('home')


class Schoollist(ListView):
    model=School
    template_name="viewlist.html"
    context_object_name="list"

class Studentlist(ListView):
    model=Student
    template_name="studentlist.html"
    context_object_name="student"

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(school__location="Ernakulam")  #foreign key field school.to compare location we use school__location
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(name__startswith="m")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(age__gt="13")
    #     return queryset

    def get_queryset(self):
        qs=super().get_queryset()
        queryset=qs.filter(age__lt="13")
        return queryset

    #get_context_data()
    def get_context_data(self):
        context=super().get_context_data()  #calling the parent get_context_data()
        context['name']='Marco'
        context['school']=School.objects.all()
        return context


class Schooldetail(DetailView):
    model=School
    template_name="schoollist.html"
    context_object_name="detail"

from django.contrib.auth.models import User
class Register(CreateView):
    model=User
    # fields=['username','password','email','first_name','last_name']
    form_class = Registerform
    template_name="register.html"
    success_url=reverse_lazy('login')

    def form_valid(self,form):        #To override the form_valid() method inside CreateView class
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']

        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('login')

from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name="login.html"

from django.views.generic import View
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
