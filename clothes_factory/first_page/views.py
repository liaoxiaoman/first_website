from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'first_page/home.html')

def product(request):
    return render(request, 'first_page/product.html')

def case(request):
    return render(request, 'first_page/case.html')

def contact(request):
    return render(request, 'first_page/contact.html')