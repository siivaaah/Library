from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

@login_required
def viewbook(request):
    b=Book.objects.all()                                     #reads all records(objects) from model(table) Book
    context={'books':b}                                       #here key is book and data is b
    return render(request,'view.html',context)  #sends the data as context to view.html


from books.models import Book
@login_required
def addbook(request):
    if(request.method=='POST'):
        #normal form fields
        tit=request.POST['t']
        aut=request.POST['a']
        pri=request.POST['p']
        lan=request.POST['l']
        pag=request.POST['pg']

        #file upload
        img=request.FILES['i']
        pdf=request.FILES['f']

        b=Book.objects.create(title=tit,author=aut,price=pri,pages=pag,language=lan,image=img,pdf=pdf)
        b.save()
        return redirect('books:home')

    return render(request,'add.html')

@login_required
def factorialofanumber(request):
    if(request.method=='POST'):
        num=int(request.POST['n'])

        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request,'fact.html',{'fact':f})
    return render(request,'fact.html')

@login_required
def bookdetails(request,i):
    b=Book.objects.get(id=i)
    context={'book':b}
    return render(request,'bookdetail.html',context)

@login_required
def deletebook(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:viewbook')

@login_required
def editbook(request,i):
    b=Book.objects.get(id=i)
    if(request.method=='POST'):
        b.title=request.POST['t']
        b.author=request.POST['a']
        b.price=request.POST['p']
        b.language=request.POST['l']
        b.pages=request.POST['pg']

        if(request.FILES.get('i')==None):
            b.save()
        else:
            b.image=request.FILES.get('i')   #if image field is not selected

        if(request.FILES.get('f')==None):
            b.save()
        else:
            b.pdf=request.FILES.get('f')

        b.save()
        return redirect('books:viewbook')

    context={'book':b}
    return render(request,'edit.html',context)

from django.db.models import Q

def searchbook(request):
    if (request.method=="POST"):
        query=request.POST['q']
        b=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

        context={'books':b}

    return render(request,'search.html',context)


