from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        n=request.POST['n']
        a=request.POST['a']

        if(p==p1):  #checks whether two passwords are same
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,phone=n,address=a)
            u.save()
            return redirect('books:home')
        else:       #password are not same
            messages.error(request,"Password are not same")


    return render(request,'regsiter.html')


from django.contrib.auth import authenticate,login,logout
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            messages.error(request,"Invalid user credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')
