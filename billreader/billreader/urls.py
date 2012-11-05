from django.conf.urls import patterns, include, url
from api.resources import v1_api
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'billreader.views.home', name='home'),
    # url(r'^billreader/', include('billreader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^load/', include('ATTparser.urls')),
    url(r'^api/', include(v1_api.urls)),

)