from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'vendor.views.home'),
    url(r'^/login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^/logout$', 'django.contrib.auth.views.logout', {'next_page': '/vendor'}),
    url(r'^/signup$', 'vendor.views.signup'),
    url(r'^/update$', 'vendor.views.update'),
)