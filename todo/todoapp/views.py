from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model = Task
    template_name = 'index1.html'
    context_object_name = 'task'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'view.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('todoapp:detailtask', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'detail.html'
    success_url = reverse_lazy('todoapp:view')


# Create your views here.

def index(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "index.html", {'task': task1})


def deletelist(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, "detail.html")


def updatelist(request, id):
    task = Task.objects.get(id=id)
    form = Todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, 'task': task})
