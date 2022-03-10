from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from todo.forms import *
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, DeleteView, DetailView, CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Task
from django.contrib import messages

class LoginUser(LoginView):
    template_name = 'todo/reg/login.html'
    extra_context = {'title':'login'}
    redirect_authenticated_user = True

class RegisterUser(FormView):
    template_name = 'todo/reg/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')
    extra_context = {'title':'registration'}
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

def test_rediretc(request):
    return redirect('tasks')

class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create_task.html'
    extra_context = {'title':'create-task'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create_task.html'
    extra_context = {'title':'update-task'}

class ShowList(LoginRequiredMixin ,ListView):
    model = Task
    template_name = 'todo/show_list.html'
    context_object_name = 'tasks'
    extra_context = {'title':'all-tasks'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowList, self).get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

def show_info(request):
    return HttpResponse(f'<h1>{request.user}</h1>')

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
    def get(self, request, *args, **kwargs):
        return super(DeleteTask, self).delete(request, *args, **kwargs)

from todo_project.settings import EMAIL_HOST_USER
def mail(request):
    subject = 'Test subject'
    message = 'Message witch will be send'
    email_from = EMAIL_HOST_USER
    email_receive = ['380992566619v@gmail.com']

    send_mail(subject, message, email_from, email_receive)
    #return redirect('tasks')

def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        rez = User.objects.filter(email=email)
        if len(rez) != 0:
            subject = 'Reset password'
            message = 'In this message will be secret code!'
            email_from = EMAIL_HOST_USER
            email_receive = [email]
            send_mail(subject, message, email_from, email_receive)
            messages.success(request, 'message was send, check your email!')
        else:
            messages.error(request, 'This email is wrong')
    return render(request, template_name='todo/reg/forget_password.html')
