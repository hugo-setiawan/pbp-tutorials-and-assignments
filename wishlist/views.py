import datetime
import json
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.utils.encoding import iri_to_uri
from django.utils.http import url_has_allowed_host_and_scheme
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
        'nama': 'Hugo',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

# show_wishlist_ajax for tutorial 5
@login_required(login_url='/wishlist/login/')
def show_wishlist_ajax(request):
    # get data from BarangWishlist model
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Hugo',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist_ajax.html", context)

# add_wishlist_json for tutorial 5
@login_required(login_url='/wishlist/login/')
def add_wishlist_json_ajax(request):
    if request.method == "POST":
        # JSON data ditaruh sbg param post di data
        data = json.loads(request.POST['data'])

        new_task = BarangWishlist(nama_barang=data["nama_barang"], harga_barang=data["harga_barang"], deskripsi=data["deskripsi"]) # probably unsafe, validate?
        new_task.save()

        # new_task dijadiin list karena paramnya harus berupa iterable
        return HttpResponse(serializers.serialize("json", [new_task]), content_type="application/json")

    return redirect('wishlist:show_wishlist_ajax')

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

            # redirect implementation https://stackoverflow.com/a/44807947
            next_url = request.GET.get('next')

            # redirect URL validation https://stackoverflow.com/a/60372947
            if next_url and url_has_allowed_host_and_scheme(next_url, None):
                next_url = iri_to_uri(next_url)
                response = HttpResponseRedirect(next_url)
            else:
                # default is normal wishlist page
                response = HttpResponseRedirect(reverse('wishlist:show_wishlist'))

            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            messages.info(request, 'Username atau Password salah!')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login_user'))
    response.delete_cookie('last_login')
    return response
