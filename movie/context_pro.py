from .models import *
# from django.contrib.auth.models import User
def view_all(request):

    context = {
        "categories":Category.objects.all(),
        "genres":Genre.objects.all(),
    }
    
    return context  