from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'product.html')

def booking(request):
    return render(request, 'booking.html')