from django.contrib import admin
from django.urls import path
from myquiz import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.authlogin, name='authlogin'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', views.authlogout, name='authlogout'),
    path('quizpage/', views.quizpage, name='quizpage'),
]
