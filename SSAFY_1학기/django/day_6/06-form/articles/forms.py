from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요',
                'maxlength':10,
            }
        )
    )
    class Meta:
        # 인스턴스 만드는거 아님!
        model = Article
        # field 라고 적으면 동작하지 않음!
        fields = '__all__'
        # exclude = ('title',)