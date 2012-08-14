# -*- coding:utf-8 -*-

from django.db import models
from account.models import Account

class Post(models.Model):
    owner = models.ForeignKey(Account, null=False)
    created = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(u'like',default=0)
    
    img_url = models.CharField(u'Img', max_length=256, null=False)
    short_name = models.CharField(u'Кароткая назва', max_length=64, null=False)
    name = models.CharField(u'Назва', max_length=256, null=False)
    text = models.TextField(u'Тэкст')
    
