from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'search.views.search'),
    url(r'^/find-vendors$', 'search.views.find_vendors')
)