from django.shortcuts import render, redirect
from .models import URL
from .utils import generate_short_url
from django.http import HttpResponsePermanentRedirect

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = generate_short_url()
        URL.objects.create(original_url=original_url, short_url=short_url)
        return render(request, 'shortened.html', {'short_url': short_url})
    return render(request, 'index.html')

def redirect_url(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return HttpResponsePermanentRedirect(url.original_url)
    except URL.DoesNotExist:
        return render(request, '404.html')