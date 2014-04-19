from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    context = {'boldmessage': "I am bold font from the context"}

    return render(request, 'tango/index.html', context)

def about(request):
	return HttpResponse("Tango says: WELCOME TO THE ABOUTS. <a href='/tango/'>Index</a>")
