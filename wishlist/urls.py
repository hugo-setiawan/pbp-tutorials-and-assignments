from django.urls import path
from wishlist.views import show_wishlist, data_xml_wishlist, data_json_wishlist, data_json_wishlist_by_id, data_xml_wishlist_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', data_xml_wishlist, name='data_xml_wishlist'),
    path('xml/<int:id>', data_xml_wishlist_by_id, name='data_xml_wishlist_by_id'),
    path('json/', data_json_wishlist, name='data_json_wishlist'),
    path('json/<int:id>', data_json_wishlist_by_id, name='data_json_wishlist_by_id'),
]