#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic.base import View
from article.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import urllib,urllib2,httplib
import json, sys, datetime
from django.db import connections
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    posts = Article.objects.order_by('-date_time')[:5]
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render_to_response("index.html", {'post_list' : post_list}, context_instance=RequestContext(request))

def detail(request, pid):
    try:
        post = Article.objects.get(id=int(pid))
    except Article.DoesNotExist :
        raise Http404
    return render_to_response("post.html", {'post' : post}, context_instance=RequestContext(request))

def archives(request) :
    try:
        posts = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'posts' : posts, 'error' : False})

def aboutme(request):
    return render_to_response("about.html", context_instance=RequestContext(request))

def contact(request):
    return render_to_response("contact.html", context_instance=RequestContext(request))