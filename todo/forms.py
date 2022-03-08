from django.forms import ModelForm, forms
from todo.models import Task
from django.contrib.auth.forms import UserCreationForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc']

class LoginForm(forms.Form):
    username = forms.Field()
    password = forms.Field()

#class RegisterForm(UserCreationForm):
