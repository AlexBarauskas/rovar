from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',
                       url(r'^login$','login',name='login'),
                       url(r'^login_$','login_to_account',name='login_to_account'),
                       url(r'^logout$','logout',name='logout'),

                       url(r'^$','main_page', name='account_main_page'),
                       url(r'^tracks$','my_tracks', name='account_my_tracks'),
                       url(r'^points$','my_points', name='account_my_points'),
                       )
