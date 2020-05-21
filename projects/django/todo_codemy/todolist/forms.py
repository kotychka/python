from django import forms
from django.forms import ModelForm

from .models import *

class ItemForm(forms.ModelForm):
	# title = forms.CharField()

	class Meta:
		model = To_do
		fields = '__all__'

