from django.shortcuts import render
from .models import ProductPost
from .forms import ProductPostForm
from django.http import HttpResponse
# Create your views here.


def indexView(request):
    if request.method == 'POST':
        product_form = ProductPostForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse('success')
    else:
        product_form = ProductPostForm()
        product_data = ProductPost.objects.all()
    return render(request, 'market_communication/index.html', {'product_form': product_form, 'product_data': product_data})
