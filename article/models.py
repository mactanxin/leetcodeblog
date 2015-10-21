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
    leedindex = models.IntegerField(null = True)
    category = models.CharField(max_length = 50, blank = True, null = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)
    # content = RichTextField()
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY, null = True)
    #p.get_shirt_size_display()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']