from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love to sell things!</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Check out our listings!</p>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Get in touch with us!</p>')