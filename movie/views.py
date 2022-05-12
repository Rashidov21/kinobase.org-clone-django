from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout


# Create your views here.
from .models import *
from .forms import UserRegisterForm


def category_list(request,slug):
    category = Category.objects.get(slug=slug) #Фильмы
    movies = Movie.objects.filter(category=category)   
    paginator = Paginator(movies, 2) # Show 2 movies per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

def my_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    
    else:
        # Return an 'invalid login' error message.
        return render(request, "registration/login.html")
    
    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    messages.add_message(request,messages.INFO,"Siz chiqdiz!") #INFO, SUCCESS, WARNING, ERROR,DEBUG
    return HttpResponseRedirect("/")

def registration_view(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,"Siz royhatdan ottiz , endi kiring!")
        return HttpResponseRedirect("/login/")
    else:
        messages.add_message(request,messages.INFO,"Xatolik!")
        return render(request, "registration/registration.html", {"form":form})

    return render(request, "registration/registration.html", {"form":form})


class HomeView(ListView):
    model = Movie
    template_name = 'index.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie-detail.html'

