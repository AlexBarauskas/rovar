# -*- coding: utf-8 -*-
from django.db import models
from jsonfield.fields import JSONField
from account.models import Account


# Create your models here.
TRACK_TYPES = (('c', 'Commuting'),
               ('rr', 'Recreational (Road)'),
               ('rm', 'Recreational (MTB)'),
               ('sr', 'Sport (Road)'),
               ('sm', 'Sport (MTB)'),
               ('o','Other')
               )
POINTS_TYPES = (('s','Shop'),
                ('p','Parking'),
                ('r','Repair'),
                ('o','Other'),
                )
DIC_TRACK_TYPES = {'c' : 'Commuting',
                   'rr': 'Recreational (Road)',
                   'rm': 'Recreational (MTB)',
                   'sr': 'Sport (Road)',
                   'sm': 'Sport (MTB)',
                   'o' : 'Other',
                   }
DIC_POINTS_TYPES = {'s':'Shop',
                    'p':'Parking',
                    'r':'Repair',
                    'o':'Other',
                    }


class Track(models.Model):
    owner = models.ForeignKey(Account, null=True)
    name = models.CharField(u'Назва', max_length=64, null=False, default="")
    description = models.TextField(u'Апiсанне', null=False, default="")
    video = models.TextField(u'Вiдэо', default="")
    track_type = models.CharField(u'Type',
                                  max_length=2,
                                  choices=TRACK_TYPES,
                                  default='c')
    data = JSONField()

    def type(self):
        return DIC_TRACK_TYPES.get(self.track_type,'Other')

class Point(models.Model):
    owner = models.ForeignKey(Account, null=True)    
    name = models.CharField(u'Назва', max_length=64, null=False, default="")
    description = models.TextField(u'Description', null=False, default="")
    point_type = models.CharField(u'Type',
                                  max_length=1,
                                  choices=POINTS_TYPES,
                                  default='o')
    place_point = JSONField()
    
    def type(self):
        return DIC_POINTS_TYPES.get(self.point_type,'Other')
