from django import forms
from .models import Game


class GameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'genre', 'price')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError('Title kamida 3 ta harfdan iborat bo\'lishi kerak!')
        return title