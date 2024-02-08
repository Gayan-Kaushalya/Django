from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello, World!</h1>
        <p>Here are the bands:</p>
        <ul>
            {"".join([f'<li>{band.name}</li>' for band in bands])}
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love to sell things!</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Check out our listings!</p>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Get in touch with us!</p>')