"""
URL configuration for moviestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name="home"),
    path('',views.Home.as_view(),name='home'),
    # path('add',views.add,name="add"),
    path('add',views.AddMovie.as_view(),name='add'),
    # path('view/<int:i>',views.view,name="view"),
    path('view/<int:pk>',views.Moviedetail.as_view(),name="view"),
    # path('edit/<int:i>',views.editmovie,name="edit"),
    path('edit/<int:pk>',views.Movieupdate.as_view(),name="edit"),
    # path('delete/<int:i>',views.deletemovie,name="delete"),
    path('delete/<int:pk>',views.Moviedelete.as_view(),name="delete"),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
