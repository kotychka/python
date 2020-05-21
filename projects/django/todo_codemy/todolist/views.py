from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import *

def index(request):

	items = To_do.objects.all
	context = {'items': items}

	if request.method=='POST':
		form = ItemForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been added to the list'))

	return render(request, 'index.html', context)

def delete(request, item_id):
	item = To_do.objects.get(pk=item_id)
	item.delete()
	messages.success(request, ('Item has been deleted'))

	return redirect('index')

def cross_off(request, item_id):
	item = To_do.objects.get(pk=item_id)
	item.completed = True
	item.save()

	return redirect('index')

def uncross(request, item_id):
	item = To_do.objects.get(pk=item_id)
	item.completed = False
	item.save()

	return redirect('index')

def edit(request, item_id):
	item = To_do.objects.get(pk=item_id)
	context = {'item': item}

	if request.method=='POST':
		form = ItemForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been edited'))

			return redirect('index')

	return render(request, 'edit.html', context)
