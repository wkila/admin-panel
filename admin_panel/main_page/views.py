from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactModelForm
from .models import ContactModel

api_req = {
    'Получить цену': {
        'get_price': {
            'Количество прокси': 'count',
            'Период': 'period'
        }
    }
}

# Create your views here.

def main_page(request):
    return render(request, 'main_page/index.html')

def dashboard(request):
    data = {
        'names_cards': ['Количество прокси', 'Баланс']
    }
    return render(request, 'main_page/dashboard.html', {'data': data})

# def contact(request):
#     return render(request, 'main_page/contact.html')

def get_form(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            current_url = request.path
            return HttpResponseRedirect(f'{current_url}thanks')
    else:
        form = ContactModelForm()
    return render(request, 'main_page/contact.html', {'form': form})

def thanks(request):
    return render(request, 'main_page/thanks.html')