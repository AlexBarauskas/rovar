# -*- coding: utf-8 -*-
from django.utils import simplejson
from account.models import Account

def change_data_add_track(request):
    coordinates = request.POST.get('coordinates',None)
    if not coordinates is None:
        coordinates = simplejson.loads(coordinates)
    video = request.POST.get('video',None)
    description = request.POST.get('description',None)
    name = request.POST.get('name',None)
    track_type = request.POST.get('track_type',None)
    email = request.POST.get('email',None)
    
    errors = {}
    
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    er_email = []
    if user is None:
        er_email.append(u'Вы павiнны увайсцi у сiстэму!')
    else:
        if email != user.email:
            er_email.append(u'Email не супадае з %s!'%user.email)
    if er_email:
        errors['email'] = er_email
    if not coordinates or len(coordinates)<2:
        errors['coordinates'] = [u'Вы павiнны дадаць больш за адзiн пункт маршруту!']
    if not name:
        errors['name'] = [u'Абавязковае поле!']
    if not description:
        errors['description'] = [u'Абавязковае поле!']
    if track_type is None:
        errors['track_type'] = [u'Абавязковае поле!']
    if errors.get('email',None) is None:
        description = '%s<hr/>%s'%(description,user)
    return [errors,{'owner':user,
                    'coordinates':coordinates,
                    'name':name,
                    'description':description,
                    'video':video,
                    'track_type':track_type}]


def change_data_add_point(request):
    place_point = request.POST.get('place_point',None)
    if not place_point is None:
        place_point = simplejson.loads(place_point)
    description = request.POST.get('description',None)
    name = request.POST.get('name',None)
    point_type = request.POST.get('point_type',None)
    email = request.POST.get('email',None)
    
    errors = {}
    
    user = request.session.get('user',None)
    if not user is None:
        user = Account.objects.get(id=user)
    er_email = []
    if user is None:
        er_email.append(u'Вы павiнны увайсцi у сiстэму!')
    else:
        if email != user.email:
            er_email.append(u'Email не супадае з %s!'%user.email)
    if er_email:
        errors['email'] = er_email
    if not place_point or len(place_point)!=2:
        errors['place_point'] = [u'Памылка у каардынатах!']
    if not name:
        errors['name'] = [u'Абавязковае поле!']
    if not description:
        errors['description'] = [u'Абавязковае поле!']
    if point_type is None:
        errors['point_type'] = [u'Абавязковае поле!']
    if errors.get('email',None) is None:
        description = '%s<hr/>%s'%(description,user)
    return [errors,{'owner':user,
                    'place_point':place_point,
                    'name':name,
                    'description':description,
                    'point_type':point_type}]

