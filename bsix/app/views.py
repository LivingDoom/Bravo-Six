from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def faq(request):
    return render(request, 'app/faq.html')

def welfare(request):
    return render(request, 'app/welfare.html')