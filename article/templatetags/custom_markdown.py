#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

#for customized filter
register = template.Library()

#register a custom filter
@register.filter(is_safe=True)  
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))