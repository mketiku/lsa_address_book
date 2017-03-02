from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^address_book/',
        include(
            "address_book.urls")),
    # url(r'^login/$', views.login,
    #     {'template_name': 'login.html',
    #      'authentication_form': LoginForm}),
    # url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]