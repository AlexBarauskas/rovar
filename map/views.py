# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from django.db.models import Max, Min

from account.models import Account
from datetime import datetime
import time

from map.models import Track, Point
from map.methods import change_data_add_track

TRACK_TYPES = {'c' : 'Commuting',
               'rr': 'Recreational (Road)',
               'rm': 'Recreational (MTB)',
               'sr': 'Sport (Road)',
               'sm': 'Sport (MTB)',
               'o' : 'Other',
               }


def all_tracks(request):
    tracks = Track.objects.all()
    data = []
    for t in tracks:
        data.append(t.data)
    data = { "type": "FeatureCollection", "features":data}
    return HttpResponse(simplejson.dumps(data),mimetype='text/json')

def add_track(request):
    errors, T = change_data_add_track(request)
    if not errors:
        errors = None
        data = {"type": "Feature",
                "properties": {"name": T['name'],
                               "description": T['description'],
                           "video" : T['video'],
                           "type": TRACK_TYPES[T['track_type']]},
            "geometry": {"type": "LineString",
                         "coordinates": T['coordinates']}}
        Track(name=T['name'],
              description = T['description'],
              track_type = T['track_type'],
              video = '',
              data = data).save()
    
    return HttpResponse(simplejson.dumps({'errors':errors,'data':T}),mimetype='text/json')
    
def all_points(request):
    data = Point.objects.all()
    points = []
    for p in data:
        points.append(p.place_point)
    data = { "type": "FeatureCollection", "features":points}
    return HttpResponse(simplejson.dumps(data),mimetype='text/json')


if Point.objects.count()==0:
    Point(name='test_point',
          description = 'test_point',
          point_type = 'r',
          place_point = {"type": 'Feature',
                         "properties": {
                             "name": "dragonshop",
                             "description": "Velomir - Specialized bikes",
                             "type": "shop"},
                         "geometry": {"type": "Point",
                                      "coordinates": [27.545, 53.85]}}
    ).save()

if Track.objects.count()==0:
    Track(name='test_track',
          description = 'test_trak',
          track_type = 'c',
          video = '',
          data = {"type": "Feature",
    "properties": {"name": "first_track",
        "description": "First track (probably bikeroad)",
        "video" : "<iframe width=\"640\" height=\"360\" src=\"https://www.youtube-nocookie.com/embed/mIwfS8uJJIk?rel=0\" frameborder=\"0\" allowfullscreen></iframe>",
        "type": "Commuting"},
    "geometry": {"type": "LineString",
        "coordinates": [ [27.55947400,53.90338100],
            [27.55944100,53.90338400],
            [27.55920700,53.90342600],
            [27.55918800,53.90343900],
            [27.55915600,53.90346400],
            [27.55912800,53.90346700],
            [27.55910000,53.90345700],
            [27.55907500,53.90344000],
            [27.55904900,53.90341300],
            [27.55904600,53.90338800],
            [27.55905800,53.90336800],
            [27.55907800,53.90335000],
            [27.55909900,53.90333100],
            [27.47844390,53.84112600],
            [27.47838790,53.84179590]]}}).save()
