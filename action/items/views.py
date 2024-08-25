from django.shortcuts import render, redirect
from .models import Items
from django.contrib.auth.decorators import login_required

@login_required
def items(request):
    items = Items.objects.filter(created_by=request.user)

    return render(request, 'items/items.html',{
        'items':items
    })

@login_required
def view_items(request, pk):
    items = Items.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'items/viewitem.html',{
        'items':items
    })


@login_required
def add_item(request):
    if request.method == "POST":
        fleet = request.POST.get('fleet', '')
        tail = request.POST.get('tail', '')
        remark = request.POST.get('remark', '')
        required_action = request.POST.get('required_action', '')
        logged = request.POST.get('logged', '')
        duedate = request.POST.get('duedate', '')
        owner = request.POST.get('owner', '')
        contact = request.POST.get('contact', '')
        level1 = request.POST.get('level1', '')
        level2 = request.POST.get('level2', '')
        level3 = request.POST.get('level3', '')
        status = request.POST.get('status', '')
        requestedby = request.POST.get('requestedby', '')
    

        if fleet:
            Items.objects.create(fleet=fleet,tail=tail,remark=remark, required_action=required_action, logged=logged, duedate=duedate,
                                 owner=owner, contact=contact, level1=level1, level2=level2, level3=level3, status=status, requestedby=requestedby, created_by=request.user)
            return redirect('/items/')
    return render(request, 'items/add.html')

@login_required
def edit_items(request, pk):
    items = Items.objects.filter(created_by=request.user).get(pk=pk)
    if request.method == "POST":
        fleet = request.POST.get('fleet', '')
        tail = request.POST.get('tail', '')
        remark = request.POST.get('remark', '')
        required_action = request.POST.get('required_action', '')
        logged = request.POST.get('logged', '')
        duedate = request.POST.get('duedate', '')
        owner = request.POST.get('owner', '')
        contact = request.POST.get('contact', '')
        level1 = request.POST.get('level1', '')
        level2 = request.POST.get('level2', '')
        level3 = request.POST.get('level3', '')
        status = request.POST.get('status', '')
        requestedby = request.POST.get('requestedby', '')

        if remark:
            items.fleet=fleet
            items.tail=tail
            items.remark=remark
            items.required_action=required_action
            items.logged=logged
            items.duedate=duedate
            items.owner=owner
            items.contact=contact
            items.level1=level1
            items.level2=level2
            items.level3=level3
            items.status=status
            items.requestedby=requestedby
            items.save()
            return redirect('/items/')
    return render(request, 'items/edit.html',{
        'items':items
    })

@login_required
def delete_items(request, pk):
    items = Items.objects.filter(created_by=request.user).get(pk=pk)
    items.delete()
    return redirect('/items/')
