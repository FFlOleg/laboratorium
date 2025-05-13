from django import forms
from .models import Choice

class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect)
