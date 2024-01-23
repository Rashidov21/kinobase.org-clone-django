
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('movie.urls', namespace='movie')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('django.contrib.auth.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    # Login
    # path("login/", LoginView.as_view(
    #     template_name=''
    # ),)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
