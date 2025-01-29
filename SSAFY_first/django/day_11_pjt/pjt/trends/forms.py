from django.forms import ModelForm
from .models import Keyword

class KeywordForm(ModelForm):
    class Meta():
        model = Keyword
        fields = '__all__'
