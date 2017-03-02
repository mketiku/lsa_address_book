from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.address_list, name='address_list'),
                       url(r'^new$', views.address_create, name='address_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.address_update, name='address_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.address_delete, name='address_delete'),
                       )
