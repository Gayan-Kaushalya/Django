from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html', 
                  {'bands':bands})  #context dictionary
    
    
    ''' I used this before 2024.03.15
    return HttpResponse(f"""
        <h1>Hello, World!</h1>
        <p>Here are the bands:</p>
        <ul>
            {"".join([f'<li>{band.name}</li>' for band in bands])}
        </ul>
    """)
    Under the hood, the  render  function creates an HttpResponse object with the HTML from our template and returns it. So our view is still returning an HttpResponse (which it must do to be a view).
    '''
    
''' Anti Pattern

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f”””
        <html>
            <head><title>Merchex</title><head>
            <body>
                <h1>Hello Django!</h1>
                <p>My favourite bands are:<p>
                <ul>
                    <li>{bands[0].name}</li>
                    <li>{bands[1].name}</li>
                    <li>{bands[2].name}</li>
                </ul>
            </body>
        </html>
    ”””)
'''


def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    return render(request, 'listings/listings.html')

def contact(request):
    return render(request, 'listings/contact.html')