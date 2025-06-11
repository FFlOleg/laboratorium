from django import forms
from .models import Temat, Notatka

class TematForm(forms.ModelForm):
    class Meta:
        model = Temat
        fields = ['nazwa', 'poziom', 'osiagniecia']

    def clean_nazwa(self):
        nazwa = self.cleaned_data['nazwa']
        if len(nazwa) < 3:
            raise forms.ValidationError("Nazwa musi mieć co najmniej 3 znaki.")
        return nazwa

class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['tresc']
