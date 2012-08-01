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
        er_email.append('Вы павiнны увайсцi у сiстэму!')
    else:
        if email != user.email:
            er_email.append('Email не супадае з %s!'%user.email)
    if er_email:
        errors['email'] = er_email
    if not coordinates or len(coordinates)<2:
        errors['coordinates'] = ['Вы павiнны дадаць больш за адзiн пункт маршруту!']
    if not name:
        errors['name'] = ['Абавязковае поле!']
    if not description:
        errors['description'] = ['Абавязковае поле!']
    if track_type is None:
        errors['track_type'] = ['Абавязковае поле!']

    return [errors,{'coordinates':coordinates,
                    'name':name,
                    'description':description,
                    'video':video,
                    'track_type':track_type}]
    
