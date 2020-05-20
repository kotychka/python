from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
	todos = TodoList.objects.all()
	categories = Category.objects.all()
	if request.method == 'POST':
		if 'taskAdd' in request.POST:
			title = request.POST['description']
			date = str(request.POST['date'])
			category = request.POST['category_select']
			content = title + '--' + date + ' ' + category
			Todo = TodoList(title=title, content=content, due_date=date, 
				category=Category.objects.get(name=category))
			Todo.save()
			return redirect('/')

		if 'taskDelete' in request.POST:
			checkedlist = request.POST['checkedbox']
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))
				todo.delete()

	context = {'todos': todos, 'categories': categories}
	return render(request, 'index.html', context)

