from django import forms
from .models import Store, Product

class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user','store',]