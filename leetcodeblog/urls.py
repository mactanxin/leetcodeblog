#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""leetcodeblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  #可以使用设置好的url进入网站后台
    url(r'^$', 'article.views.home'),
    url(r'^(?P<pid>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^about', 'article.views.aboutme'),
    url(r'^archives','article.views.archives'),
    url(r'^contact', 'article.views.contact'),
    url(r'^summernote/', include('django_summernote.urls')),
)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )