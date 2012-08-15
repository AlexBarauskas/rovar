# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'blog.views',
    url(r'^(?P<post_id>\d+)/add-like$','add_like', name='add-like'),
    
    )
