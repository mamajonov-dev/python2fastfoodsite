from django.shortcuts import (render, redirect,
                              HttpResponseRedirect)
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *

def home(request):
    maxsulotlar = ProductModel.objects.all()
    context = {
        'productlar': maxsulotlar
    }
    return render(request, 'index.html', context)

def karkinkagaqoshish(request, product_id):
    product = ProductModel.objects.get(id=product_id)
    try:
        karzinka = KarzinkaModel.objects.get(product=product, owner=request.user, completed=False)
        karzinka.count += 1
        karzinka.save()
    except:
        cart = KarzinkaModel.objects.create(
            owner=request.user,
            product=product
        )
        cart.save()
    return redirect('home')

def karzinkanikorish(request):
    karzinkalar = KarzinkaModel.objects.filter(owner=request.user, completed=False)
    context = {
        'karzinkalar': karzinkalar
    }
    return render(request, 'karzinka.html', context)


def registrview(request):
    form = RegisterFrom()
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('karzinkanikorish')

    context = {
        'form': form
    }
    return render(request, 'form.html', context)

def loginview(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context  = {
        'form': form
    }
    return render(request, 'form.html',context)



def deletecartitem(request, cart_id):
    cart = KarzinkaModel.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def addorder(request):
    form = OrderForm()
    karzinkalr = KarzinkaModel.objects.filter(owner=request.user,
                                             completed=False)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            qabul_qiluvchi = form.cleaned_data['qabul_qiluvchi']
            for karzinka in karzinkalr:
                order = OrderModel.objects.create(
                    owner=request.user,
                    address=address,
                    phone=phone,
                    qabul_qiluvchi=qabul_qiluvchi,
                    karzikna=karzinka
                )
                order.save()

                karzinka.completed=True
                karzinka.save()
            return redirect('karzinkanikorish')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)


