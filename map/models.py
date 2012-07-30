# -*- coding: utf-8 -*-
from django.db import models
from jsonfield.fields import JSONField

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

class Track(models.Model):
    name = models.CharField(u'Назва', max_length=64, null=False, default="")
    description = models.CharField(u'Description', max_length=64, null=False, default="")
    video = models.TextField('Вiдэо', default="")
    track_type = models.CharField(u'Type',
                                  max_length=2,
                                  choices=TRACK_TYPES,
                                  default='c')
    data = JSONField()


class Point(models.Model):
    name = models.CharField(u'Назва', max_length=64, null=False, default="")
    description = models.CharField(u'Description', max_length=64, null=False, default="")
    point_type = models.CharField(u'Type',
                                  max_length=1,
                                  choices=POINTS_TYPES,
                                  default='o')
    place_point = JSONField()
    
