from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# show_wishlist view as defined in tutorial document
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    # get data from BarangWishlist model
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Hugo'
    }
    return render(request, "wishlist.html", context)

def data_xml_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), content_type="applicaton/xml")

def data_xml_wishlist_by_id(request, id):
    data_barang_wishlist_by_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist_by_id), content_type="application/xml")

def data_json_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), content_type="application/json")

def data_json_wishlist_by_id(request, id):
    data_barang_wishlist_by_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_barang_wishlist_by_id), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login_user')
    
    context = {
        'form': form
    }

    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('wishlist:show_wishlist')

        else:
            messages.info(request, 'Username atau Password salah!')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('wishlist:login_user')
