from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'django_hosting_app/home.html')

