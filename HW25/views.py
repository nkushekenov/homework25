from django.shortcuts import render, redirect
from .forms import IceCreamForm

def add_icecream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = IceCreamForm()

    return render(request, 'add_icecream.html', {'form': form})

def success(request):
    return render(request, 'success.html')
