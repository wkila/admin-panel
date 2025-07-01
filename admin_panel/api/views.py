from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import weathermap
from main_page import forms

api_key = 'ac1e1a88b8-0075e8d73d-9e27ab2655'

data_db = {
    'Узнать цену': 'getprice',
    'Узнать количество': 'getcount',
    'Покупка': 'buy'
}

# Create your views here.

def get_products(request):
    data_names = data_db
    form_getprice = forms.GetPrice(prefix='getprice')
    form_getcount = forms.GetCount(prefix='getcount')
    form_buy = forms.Buy(prefix='buy')
    forms_dict = [form_getprice, form_getcount, form_buy]

    return render(request, 'api/products.html', {
        'data_names': data_names,
        'forms_dict': forms_dict,
        'form_getprice': form_getprice,
        'form_getcount': form_getcount,
        'form_buy': form_buy
    })

def send_api(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.dict()
        response = weathermap.Proxy6(api_key)
        if action == 'getprice':
            count = int(params.get('count', 1))
            period = int(params.get('period', 1))
            data = response.getprice(count, period)
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Uknown action'}, status=400)
    else:
        return JsonResponse({'error': 'POST required'}, status=405)