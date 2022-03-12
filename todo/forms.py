from django.forms import ModelForm, forms
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc']

class LoginForm(forms.Form):
    username = forms.Field()
    password = forms.Field()

