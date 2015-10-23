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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ip = __get_client_ip(request)
        if name and email and message and ip:
            msg = EmailMessage.objects.create(name = name, email_address = email, message = message, ip_address = ip)
            msg.save()
    return render_to_response("contact.html", context_instance=RequestContext(request))

def __get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def __get_last_email_from_this_ip(ip_address):
    try:
        if EmailMessage.objects.filter(ip_address=ip_address):
            em = EmailMessage.objects.filter(ip_address=ip_address)[0]
            return em
    except:
        return False

def __send_email(name,message,email):
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
