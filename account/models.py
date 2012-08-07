# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField('username', max_length=30, unique=True, help_text=u"Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters")
    email = models.EmailField('e-mail address', blank=True)
    is_active = models.BooleanField('active', default=True, help_text=u"Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    is_admin = models.BooleanField('admin', default=False)

    def __unicode__(self):
        return self.email
    
    def get_and_delete_messages(*args):
        return None
