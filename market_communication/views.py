from django.shortcuts import render

# Create your views here.


def indexView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = ProfileForm()
    return render(request, 'market_communication/index.html')
