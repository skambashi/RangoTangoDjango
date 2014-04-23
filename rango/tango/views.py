from django.shortcuts import render
from django.http import HttpResponse
from tango.models import Category, Page
from tango.forms import CategoryForm, PageForm

def encode(str):
	return str.replace(' ', '_')
	
def decode(str):
	return str.replace('_', ' ')

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context = {'categories': category_list, 'pages' : page_list}
	
	for category in category_list:
		category.url = encode(category.name)

	return render(request, 'tango/index.html', context)

def about(request):
	context = {'messagio':['My', 'name', 'is', 'Seikun', 'Kambashi']}

	return render(request, 'tango/about.html', context)
	
def category(request, category_name_url):
	category_name = decode(category_name_url)
	context = {'category_name' : category_name}
	
	try:
		category = Category.objects.get(name = category_name)
		pages = Page.objects.filter(category = category)
		
		context['pages'] = pages
		context['category'] = category
	
	except Category.DoesNotExist:
		pass
	
	return render(request, 'tango/category.html', context)

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			
			return index(request)
		
		else:
			print form.errors
	
	else:
		form = CategoryForm()
	
	return render(request, 'tango/add_category.html', {'form':form})










