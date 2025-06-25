from django import forms
from .models import Hazard, MitigationNote

class HazardForm(forms.ModelForm):
    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Hazard
        fields = ['latitude', 'longitude', 'description', 'severity', 'status']

class MitigationNoteForm(forms.ModelForm):
    class Meta:
        model = MitigationNote
        fields = ['note', 'photo', 'author_name']
