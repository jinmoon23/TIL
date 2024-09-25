from django import forms
from .models import Travels

class TravelForm(forms.ModelForm):
    plan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'ex) 슉.슈슉.'
            }
        )
    )
    start_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '2022-02-22'
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '2022-02-22'
            }
        )
    )
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'ex) 제주도'
            }
        )
    )
    class Meta:
        model = Travels
        fields = '__all__'