from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Tango says: HOLA, TODO EL MUNDO! <a href = '/tango/about'>About</a>")

def about(request):
	return HttpResponse("Tango says: WELCOME TO THE ABOUTS. <a href='/tango/'>Index</a>")
