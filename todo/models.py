from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=190)
    desc = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    #temporarily url
    def get_absolute_url(self):
        return reverse('tasks')

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'p_id':self.pk})