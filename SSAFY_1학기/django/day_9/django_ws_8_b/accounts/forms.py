from django import forms
# 1. 여기서 AuthenticationForm을 정의하는 것 같지만!
# 이미 필요한 모든것이 정의되어 있기 때문에 상속받아 재정의하는 과정이 필요없다.
# 따라서 곧바로 views 함수에서 import 받아 사용한다. 
# from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())