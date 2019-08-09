from django import forms
from .models import Mission

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['mission_number','mission_name']