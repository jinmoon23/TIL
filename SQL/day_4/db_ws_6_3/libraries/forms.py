from django import forms
from .models import Author, Book

class CreateAuthorform(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['user','subscribed_users',]

class CreateNovelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'