from django.shortcuts import redirect
from django.urls import path
from django.http import HttpResponse
from todo import views



urlpatterns = [
    path('', views.ShowList.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('update-task/<int:pk>', views.UpdateTask.as_view(), name='update'),
    path('d/<int:pk>', views.DeleteTask.as_view()),
    path('task/<int:pk>/', views.ShowTask.as_view()),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='todo/reg/logout.html'), name='logout'),
    path('registration/', views.RegisterUser.as_view(), name='register'),
    path('info/', views.show_info),
    path('send-mail/', views.mail),
    path('forget-password/', views.forget_password, name='f-password')
]