from django.shortcuts import render,redirect
from myapp.todo.models import Todo
from .forms import TodoForm 
# Create your views here.
def index(request):
    queryset = Todo.objects.all()
    form = TodoForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "queryset":queryset,
        "form":form
    }
    return render(request, 'index.html', context)

def Done(request,id):
	query = Todo.objects.get(id=id)
	query.done = True
	query.save()
	return redirect('index')

def NotDone(request,id):
	query = Todo.objects.get(id=id)
	query.done = False
	query.save()
	return redirect('index')

def delete(request,id):
	query = Todo.objects.get(id=id)
	query.delete()
	return redirect('index')