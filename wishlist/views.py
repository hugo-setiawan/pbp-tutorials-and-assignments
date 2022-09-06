from django.shortcuts import render
from wishlist.models import BarangWishlist

# show_wishlist view as defined in tutorial document
def show_wishlist(request):
    # get data from BarangWishlist model
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Hugo'
    }
    return render(request, "wishlist.html", context)