# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('rovar_admin.views',
                       url(r'^$','index', name='admin_index'),
                       url(r'^tracks$','list_tracks', name='admin_list_tracks'),
                       url(r'^tracks/delete$','delete_tracks', name='admin_delete_tracks'),
                       url(r'^points$','list_points', name='admin_list_points'),
                       url(r'^points/delete$','delete_points', name='admin_delete_points'),
                       )
