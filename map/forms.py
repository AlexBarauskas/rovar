# -*- coding: utf-8 -*-
from django import forms
from map.models import Track, Point, TRACK_TYPES

class AddTrackForm(forms.ModelForm):
    track_type = forms.ChoiceField(label=u'Тып маршруту',required=True,
                                   choices=TRACK_TYPES)
    coordinates = forms.CharField(widget=forms.HiddenInput)
    
    class Meta():
        model = Track
        fields = ('name', 'description', 'track_type','video')
