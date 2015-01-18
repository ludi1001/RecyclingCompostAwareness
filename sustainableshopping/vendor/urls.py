from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'vendor.views.home'),
    url(r'^/login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^/signup$', 'vendor.views.signup')
)