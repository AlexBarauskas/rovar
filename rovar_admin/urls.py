# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'rovar_admin.views',
    url(r'^$','index', name='admin_index'),
    url(r'^tracks$','list_tracks', name='admin_list_tracks'),
    #url(r'^tracks/delete$','delete_tracks', name='admin_delete_tracks'),
    url(r'^points$','list_points', name='admin_list_points'),
    #url(r'^points/delete$','delete_points', name='admin_delete_points'),
    
    url(r'^posts$','list_posts', name='admin_list_posts'),
    url(r'^posts/add$','edit_add_post',{'post_id':None}, name='admin_add_post'),
    url(r'^posts/(?P<post_id>\d+)/$','edit_add_post', name='admin_edit_post'),
    url(r'^(?P<name>\w+)/delete$','delete_objects', name='admin_delete_objects'),

    )
