#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    """docstring for Article"""
    DIFFICULTY = (
        ('E', 'easy'),
        ('M', 'medium'),
        ('H', 'hard'),
    )
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 200, null = True)
    leedindex = models.IntegerField(blank = True, null = True)
    category = models.CharField(max_length = 50, blank = True, default = '')
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(default = '', null = True)
    # content = RichTextField()
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY,default = '', null = True)
    #p.get_shirt_size_display()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

class EmailMessage(models.Model):
    """docstring for EmailMessage"""
    name = models.CharField(max_length = 100)
    message = models.TextField(blank = True, null = True)
    date_time = models.DateTimeField(auto_now_add = True)
    email_address = models.EmailField(max_length = 254)
    ip_address = models.GenericIPAddressField()

    def __unicode__(self):
        return self.email_address

    class Meta:
        ordering = ['-date_time']