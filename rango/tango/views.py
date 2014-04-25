from django.shortcuts import render
from django.http import HttpResponse
from tango.models import Category, Page
from tango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

def encode(str):
	return str.replace(' ', '_')
	
def decode(str):
	return str.replace('_', ' ')

def index(request):
	category_list = Category.objects.order_by('-likes')#[:5]
	page_list = Page.objects.order_by('-views')#[:5]
	context = {'categories': category_list, 'pages' : page_list}
	
	for category in category_list:
		category.url = encode(category.name)

	return render(request, 'tango/index.html', context)

def about(request):
	context = {'messagio':['My', 'name', 'is', 'Seikun', 'Kambashi']}

	return render(request, 'tango/about.html', context)
	
def category(request, category_name_url):
	category_name = decode(category_name_url)
	context = {'category_name' : category_name, 'category_name_url' : category_name_url}
	
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
			form = CategoryForm()
	
	else:
		form = CategoryForm()
	
	return render(request, 'tango/add_category.html', {'form':form})

def add_page(request, category_name_url):
	category_name = decode(category_name_url)

	if request.method == 'POST':
		form = PageForm(request.POST)
		
		if form.is_valid():
			page = form.save(commit=False)
			
			try:
				cat = Category.objects.get(name=category_name)
				page.category = cat
			except Category.DoesNotExist:
				request.method = 'GET'
				return render(request, 'tango/add_category.html', {})
			
			page.views = 0
			page.save()
			
			return category(request, category_name_url)
		
		else:
			print form.errors

	else:
		form = PageForm()
	
	return render(request, 'tango/add_page.html', {'category_name_url':category_name_url,
		'category_name':category_name, 'form':form})

def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			
			profile.save()
			
			registered = True
			
		else:
			print user_form.errors, profile_form.errors
	
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'tango/register.html', {'user_form':user_form,
		'profile_form':profile_form, 'registered':registered})








