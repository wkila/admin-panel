from django import forms
from django.forms import ModelForm
from .models import ContactModel
# Create your models here.

class ContactModelForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'textarea']
        labels = {
            'name': 'Ваше имя',
            'email': 'Электронная почта',
            'textarea': 'Ваше сообщение'
        }