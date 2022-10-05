from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_ajax, data_xml_wishlist, data_json_wishlist, data_json_wishlist_by_id, data_xml_wishlist_by_id, register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('xml/', data_xml_wishlist, name='data_xml_wishlist'),
    path('xml/<int:id>', data_xml_wishlist_by_id, name='data_xml_wishlist_by_id'),
    path('json/', data_json_wishlist, name='data_json_wishlist'),
    path('json/<int:id>', data_json_wishlist_by_id, name='data_json_wishlist_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]