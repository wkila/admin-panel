from django.urls import path
from . import views
from api import views as api_

urlpatterns = [
    path('',  views.main_page, name='mainpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.get_form, name='contact'),
    path('contact/thanks', views.thanks, name='thanks'),
    path('products/', api_.get_products, name='products'),
    path('products/send_api', api_.send_api, name='api_products')
]

