from django.shortcuts import render,redirect
from .models import Tasks
from todo_app.modelform import TasksForm,UpdateForm
from django.http import HttpResponseRedirect

# Create your views here.
def create(request):
	tasks = Tasks.objects.all()
	if request.method == 'POST':
		fm = TasksForm(request.POST)
		if fm.is_valid():
			fm.save()
			fm = TasksForm()
	else:
		fm = TasksForm()
	context = {'tasks':tasks,'form':fm}
	return render(request,'Todoapp.html',context)


def update(request, id):
	if request.method == 'POST':
		m = Tasks.objects.get(id=id)
		p = UpdateForm(request.POST,instance=m)
		if p.is_valid():
			p.save()
			return HttpResponseRedirect('/')
	else:
		m = Tasks.objects.get(id=id)
		p = UpdateForm(instance=m)
	return render(request,'Todoapp2.html',{'form': p })


def delete(request,task_id):
	if request.method == 'POST':
		task = Tasks.objects.get(id=task_id)
		task.delete()
		return HttpResponseRedirect('/')
	return render(request,'Todoapp.html')

'''def update(request, id):
	try:
		book_sel = Tasks.objects.get(id = id)
	except Tasks.DoesNotExist:
		return HttpResponseRedirect('/')
	book_form = UpdateForm(request.POST or None, instance = book_sel)
	if book_form.is_valid():
		book_form.save()
		return HttpResponseRedirect('/')
	return render(request, 'Todoapp2.html', {'form':book_form}) '''         

def delete_complete(request):
	a = Tasks.objects.filter(complete__exact=True).delete()
	return HttpResponseRedirect('/')

def delete_all(request):
	a = Tasks.objects.all().delete()
	return HttpResponseRedirect('/')
