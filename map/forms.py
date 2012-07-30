from django import forms
from map.models import Track, Point, TRACK_TYPES

class AddTrackForm(forms.ModelForm):
    track_type = forms.ChoiceField(required=True,
                                   choices=TRACK_TYPES)
    class Meta():
        model = Track
        fields = ('name', 'description', 'track_type','video')
