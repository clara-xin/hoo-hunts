from django import forms
from .models import Clue

class HuntForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['title', 'created_by', 'location', 'clue_text', 'hint_text']
        hidden_fields = {'is_active' : forms.HiddenInput()}
