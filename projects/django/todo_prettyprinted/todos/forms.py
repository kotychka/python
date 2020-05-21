from django import forms
from django.forms import ModelForm

from .models import *

class ItemForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(
		attrs = {'class':'form-control', 
		'placeholder':'Add some tasks here...', 
		'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

	class Meta:
		model = Item
		# fields = ['title']
		fields = '__all__'