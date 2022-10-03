from pickle import FALSE
from django import forms
from .models import Pets, year_choices, current_year


speciesChoices = (
    ('1', 'dog'),
    ('2', 'cat'),
    ('3', 'hamster'),)

class petForm(forms.ModelForm):

    
    species = forms.TypedChoiceField(choices = speciesChoices)
    year = forms.TypedChoiceField(coerce=int, choices = year_choices, initial=current_year)
    class Meta:
        model = Pets
        fields = ['name', 'species','year']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if len(name) == 0:
            raise forms.ValidationError("Please enter a name")

