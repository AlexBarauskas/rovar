# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('map.views',
                       url(r'^tracks$','all_tracks', name='get_all_tracks'),
                       url(r'^add-track$','add_track', name='add_track'),
                       url(r'^points$','all_points', name='get_all_oints'),
                       url(r'^add-point$','add_point', name='add_point'),
                       #url(r'wall/(?P<task_id>\d+)/del-task/','del_wall_task', name='del_wall_task'),
                       )
