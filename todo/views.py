from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from todo.forms import *
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

def main(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return HttpResponse('<h1>You are authenticated!')

# def first(request):
#     form = TaskForm()
#     return render(request, 'todo/test.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            user = authenticate(form.cleaned_data)
            #print(form.cleaned_data['username'])
            x = LoginView()
    form = LoginUser()

    return render(request, 'todo/test.html', {'form':form})

def test(request, id):
    return HttpResponse(f'Hello, your number is - {id}')

class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create_task.html'
    extra_context = {'title':'create-task'}
    # def get_context_data(self, **kwargs):
    #     context = super(CreateTask, self).get_context_data()
    #     context['title'] = 'create-task'
    #     return context

class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create_task.html'
    extra_context = {'title':'update-task'}



class ShowList(ListView):
    model = Task
    template_name = 'todo/show_list.html'
    context_object_name = 'tasks'
    extra_context = {'title':'all-tasks'}


class ShowTask(DetailView):
    model = Task
    template_name = 'todo/show_task.html'
    extra_context = {'title': 'update-task'}
    #content_object_name = 'tasks'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = self.kwargs['pk']
        return context


class DeleteTask(DeleteView):
    model = Task
    template_name = 'todo/show_task.html'
    content_object_name = 'task'
    success_url = reverse_lazy('tasks')
    #def delete(self, request, *args, **kwargs):

    def get(self, request, *args, **kwargs):
        return super(DeleteTask, self).delete(request, *args, **kwargs)
