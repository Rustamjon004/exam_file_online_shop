from django.shortcuts import render, redirect

def product_list(request):
    return render(request, 'online_shop/home.html')
# Create your views here.
