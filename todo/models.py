from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=190)
    desc = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    executed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.title

    #temporarily url
    def get_absolute_url(self):
        return reverse('tasks')

class Reset_password_code(models.Model):
    code = models.CharField(max_length=100)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='get_code')
    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'p_id':self.pk})