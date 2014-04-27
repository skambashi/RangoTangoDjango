from django import forms
from tango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Enter a category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	# inline class (didn't know you could do those... cool) for extra info on form
	class Meta:
		# associates ModelForm with Category model
		model = Category

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Enter a page title.")
	url = forms.URLField(max_length=200, help_text="Enter the URL address.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Page
		# note: hiding category - foreignkey
		fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Username")
	email = forms.CharField(help_text="E-mail")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Password")

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Website", required=False)
	picture = forms.ImageField(help_text="Profile Picture", required=False)

	class Meta:
		model = UserProfile
		fields = ['website', 'picture']
