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

class GetPrice(forms.Form):
    count = forms.CharField(label='Количество прокси',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'количество прокси'
        }
    ))
    days = forms.CharField(label='Период в днях',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите период в днях'
        }
    ))

    def do_name(self):
        str_name = self.__class__.__name__
        return str_name.lower()

class GetCount(forms.Form):
    country = forms.CharField(label='Страна',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'укажите странау в формате iso2'
        }
    ))

    def do_name(self):
        str_name = self.__class__.__name__
        return str_name.lower()

class Buy(forms.Form):
    count = forms.CharField(label='Количество прокси',
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'количество прокси'
    }
    ))

    days = forms.CharField(label='Период в днях',
       widget=forms.TextInput(attrs={
           'class': 'form-control',
           'placeholder': 'Введите период в днях'
       }
       ))

    country = forms.CharField(label='Страна',
      widget=forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'укажите странау в формате iso2'
      }
      ))

    def do_name(self):
        str_name = self.__class__.__name__
        return str_name.lower()

