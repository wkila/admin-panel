from django.urls import path
from . import views

urlpatterns = [
    path('',  views.main_page, name='mainpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.get_form, name='contact'),
    path('contact/thanks', views.thanks, name='thanks')
]

