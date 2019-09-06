from django.shortcuts import render,redirect,get_object_or_404
from myapp.todo.models import Todo
from django.db.models import F
from .forms import TodoForm 
# Create your views here.
def index(request):
    queryset = Todo.objects.all().order_by('-priority_flag',F('dueDate').desc(nulls_last=True),'done')
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

def Delete(request,id):
	query = Todo.objects.get(id=id)
	query.delete()
	return redirect('index')

def Modify(request,id):
    post = get_object_or_404(Todo,id=id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=post)
    
    return render(request, 'modify.html', {'form':form})
