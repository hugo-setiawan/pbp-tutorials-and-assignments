from django.shortcuts import render

# show_wishlist view as defined in tutorial document
def show_wishlist(request):
    return render(request, "wishlist.html")