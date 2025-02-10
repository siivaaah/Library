from django.shortcuts import render,redirect


# def home(request):
#     b=Movie.objects.all()
#     context={'movie':b}
#     return render(request,'home.html',context)


from movie.models import Movie
from django.views.generic import ListView,UpdateView


class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"


from movie.models import Movie

# def add(request):
#     if (request.method == 'POST'):
#         t = request.POST['t']
#         d = request.POST['d']
#         l = request.POST['l']
#         y = request.POST['y']
#         i = request.FILES['i']
#
#         b = Movie.objects.create(title=t,desc=d,year=y,language=l,image=i)
#         b.save()
#         return redirect('home')
#     return render(request,'add.html')

from django.views.generic import CreateView,DetailView,DeleteView
from django.urls import reverse_lazy

class AddMovie(CreateView):
    template_name="add1.html"
    fields=['title','desc','language','year','image']
    model=Movie
    success_url=reverse_lazy('home')


# def view(request,i):
#     b=Movie.objects.get(id=i)
#     context = {'movie': b}
#     return render(request,"view.html",context)

class Moviedetail(DetailView):
    model=Movie
    template_name='view.html'
    context_object_name="movie"

# def editmovie(request,i):
#     b=Movie.objects.get(id=i)
#     if(request.method=='POST'):
#         b.title=request.POST['t']
#         b.desc=request.POST['d']
#         b.language=request.POST['l']
#         b.year=request.POST['y']
#
#         if (request.FILES.get('i') == None):
#             b.save()
#         else:
#             b.image = request.FILES.get('i')
#
#         b.save()
#         return redirect('home')
#
#     context={'movie':b}
#     return render(request,'edit.html',context)

class Movieupdate(UpdateView):
    template_name="update.html"
    fields = ['title', 'desc', 'language', 'year', 'image']
    model = Movie
    success_url = reverse_lazy('home')


# def deletemovie(request,i):
#     b=Movie.objects.get(id=i)
#     b.delete()
#     return redirect('home')

class Moviedelete(DeleteView):
    template_name='delete.html'
    model=Movie
    success_url=reverse_lazy('home')




