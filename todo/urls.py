from django.urls import path
from django.http import HttpResponse
from todo import views



urlpatterns = [
    #path('', first, name='home'),
    #path('login', views.login, name='login'),
    path('', views.ShowList.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('update-task/<int:pk>', views.UpdateTask.as_view(), name='update'),
    path('d/<int:pk>', views.DeleteTask.as_view()),
    path('task/<int:pk>/', views.ShowTask.as_view()),
    #path('login/', views.LoginUser.as_view(), name='login'),
    path('login/', views.LoginView.as_view(template_name = 'todo/reg/login.html'), name='login')
]