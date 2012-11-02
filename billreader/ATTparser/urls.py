from django.conf.urls import patterns, url
from ATTparser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)$', views.loaddata, name='data')
)