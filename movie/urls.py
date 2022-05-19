from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name= 'movie'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("category/<slug>", views.category_list, name='category_list'),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name='detail'),
    path("search/", views.search, name='search'),

    # SORTING 
    path("films/<str:sort_params>", views.movie_sorting, name="sort"),


    # login 
    path("login/", views.my_login, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("registration/", views.registration_view, name='register'),

    # RESET PASSWORD 

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "registration/recover.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name ='password_reset_complete')
]