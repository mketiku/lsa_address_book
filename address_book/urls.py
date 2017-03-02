from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.AddressList.as_view(), name='address_list'),
    url(r'^new$', views.AddressCreate.as_view(), name='address_new'),
    url(r'^edit/(?P<pk>\d+)$', views.AddressUpdate.as_view(), name='address_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.AddressDelete.as_view(), name='address_delete'),
]
