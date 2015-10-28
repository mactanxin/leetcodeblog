#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'leetcodeblog.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leetcodeblog.settings")
 
 
# 上面两行测试不对，然后从stackflow上面看到了下面两行，测试ok
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()
