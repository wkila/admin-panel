from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactModelForm
from .models import ContactModel

# Create your views here.

def main_page(request):
    data = {
        'navbar': ['Dashboard', 'Products', ]
    }
    return render(request, 'main_page/index.html')

def dashboard(request):
    return render(request, 'main_page/dashboard.html')

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