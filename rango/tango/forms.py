from django import forms
from tango.models import Category, Page

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
