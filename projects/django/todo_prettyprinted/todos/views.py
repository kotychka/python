from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import *
from .forms import *
# Create your views here.
def index(request):
	items = Item.objects.all()

	form = ItemForm()

	context = {'items': items, 'form': form}
	return render(request, 'index.html', context)

@require_POST
def addItem(request):
	form = ItemForm(request.POST)

	if form.is_valid():
		form.save()

	return redirect('index')

def completeItem(request, item_id):
	item = Item.objects.get(pk=item_id)
	item.complete = True
	item.save()

	return redirect('index')

def deleteCompleted(request):
	Item.objects.filter(complete__exact = True).delete()

	return redirect('index')

def delete(request):
	Item.objects.all().delete()

	return redirect('index')

