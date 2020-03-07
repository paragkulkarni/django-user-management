from django.shortcuts import render

# Create your views here.


def indexView(request):
    return render(request, 'market_communication/index.html')
