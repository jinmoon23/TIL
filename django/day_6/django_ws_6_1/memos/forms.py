from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label = '요약',
        widget= forms.TextInput(
            attrs={
            'placeholder': 'summary',
            }
        )
    )
    memo = forms.CharField(
        label = '메모',
        widget= forms.TextInput(
            attrs= {
            'placeholder': 'memo',
            'width':50,
            'height': 5,        
            }
        )
    )
    class Meta:
        model = Memo
        fields = '__all__'