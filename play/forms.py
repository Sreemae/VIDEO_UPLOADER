from django import forms
from django.forms import ModelForm
from .models import Video

class VideoForm(ModelForm ):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
    #   widgets = {'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter here' })}
