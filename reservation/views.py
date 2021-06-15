from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'reservation/home.html', context)

def login(request):
    context={}
    return render(request, 'reservation/login.html', context)

def registration(request):
    context={}
    return render(request, 'reservation/registration.html', context)