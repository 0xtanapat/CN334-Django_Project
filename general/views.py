from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def ecommerce_index_view(request):
#     '''This function render index page of ecommerce views'''
#     return HttpResponse('Welcome to 6410742388 Tanapat Dejchodanan views!')

# def item_view(request, item_id):
#     context_data = {
#         "item_id": item_id
#     }
#     return render(request, 'index.html', context = context_data)

def homepage(request):
    return HttpResponse('Homepage')

def category(request):
    return HttpResponse('Category page')

def product(request):
    return HttpResponse('Product page')

def checkout(request):
    return HttpResponse('Checkout page')

def contact(request):
    return HttpResponse('Contact page')
