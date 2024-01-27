from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect ,HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from transliterate import translit


# Create your views here.
from .models import *
from .forms import UserRegisterForm, CommentForm


def category_list(request,slug):
    category = Category.objects.get(slug=slug) #Фильмы
    movies = Movie.objects.filter(category=category)   
    paginator = Paginator(movies, 12) # Show 2 movies per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj, "cat_name":category.name})

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
    # print(dir(form))
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

class MovieDetailView(FormMixin,DetailView):
    model = Movie
    template_name = 'movie-detail.html'
    form_class = CommentForm


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()       
        form = self.get_form()
        if form.is_valid():          
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # @staticmethod
    def get_success_url(self):
        return reverse_lazy("movie:detail", kwargs={"slug":self.object.slug})

    def form_valid(self, form):
        f = form.save(commit=False)
        f.movie = self.object
        f.save()
        return super().form_valid(form)


def search(request):
    q = request.GET.get("query")
    ru_text = translit(q, "ru").title()
    print(ru_text)
    data = Movie.objects.filter(
        Q(title__icontains=ru_text) | Q(actors__name__icontains=ru_text) | Q(genres__name__icontains=ru_text)
    )

    return render(request, 'search_list.html', {"object_list":set(data)})

def movie_sorting(request, sort_params):
    # sort_params.split("=")[0] sort type 
    # sort_params.split("=")[1] sort value
    sort_type = sort_params.split("=")[0]
    sort_value = sort_params.split("=")[1]
    # print(sort_type)
    # print(sort_params)
    if sort_type == "genres":
        genre = Genre.objects.get(id=sort_value)
        object_list = Movie.objects.filter(genres=sort_value)
        return render(request, "index.html", {"object_list":object_list, "filter_category":genre.name})
    elif sort_type == "year":
        object_list = Movie.objects.filter(year=sort_value)
        return render(request, "index.html", {"object_list":object_list, "filter_category":sort_value})
    elif sort_type == "quality":
        object_list = Movie.objects.filter(quality=sort_value)
        return render(request, "index.html", {"object_list":object_list, "filter_category":sort_value})
    else:
        print("ERROR" * 10)
        return HttpResponseRedirect("/")
    


def likeMovie(request):
    if request.user.is_authenticated:
        print(request.GET.get("data"))
    else:
        return JsonResponse({"status":400})
    return JsonResponse({"status":200})

def likedMovies(request):
    return render(request, "liked-movies.html")
