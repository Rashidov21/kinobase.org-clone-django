from django.urls import path
from .import views

app_name= 'movie'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("category/<slug>", views.category_list, name='category_list'),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name='detail'),


    # login 
    path("login/", views.my_login, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("registration/", views.registration_view, name='register'),
    path("recover/", views.recover_view, name='recover'),
]