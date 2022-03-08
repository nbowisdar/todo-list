from django.shortcuts import redirect
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
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='todo/reg/logout.html'), name='logout'),
    path('registration/', views.registration, name='register'),
    path('test-redirect/', views.register_request)
]