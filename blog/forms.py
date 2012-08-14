# -*- coding: utf-8 -*-
from django import forms
from blog.models import Post

class AddPost(forms.ModelForm):
    class Meta():
        model = Post
        #fields = ('name', 'description', 'track_type','video')
