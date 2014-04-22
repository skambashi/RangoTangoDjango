from django.shortcuts import render
from django.http import HttpResponse
from tango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context = {'categories': category_list}

	return render(request, 'tango/index.html', context)

def about(request):
	context = {'messagio':['My', 'name', 'is', 'Seikun', 'Kambashi', '.']}

	return render(request, 'tango/about.html', context)
