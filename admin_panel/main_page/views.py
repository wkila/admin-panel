from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main_page/index.html')

def dashboard(request):
    return render(request, 'main_page/dashboard.html')