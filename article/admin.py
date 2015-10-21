#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from article.models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ArticleAdmin(SummernoteModelAdmin):
    change_form_template = 'admin/change_form.html'

admin.site.register(Article, ArticleAdmin)