from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from items.models import Items

@login_required
def index(request):
    items = Items.objects.values
    return render(request, 'core/index.html',{
        'items':items})

@login_required
def about(request):
    return render(request, 'core/about.html')
'''
@login_required
def view_all(request, pk):
    items = Items.objects.values

    return render(request, 'core/viewall.html',{
        'items':items
    })

'''



