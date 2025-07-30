from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'amazon/home.html')
def contact(request):
    return render(request, 'amazon/contact.html')
def product(request):
    return render(request, 'amazon/product.html')


