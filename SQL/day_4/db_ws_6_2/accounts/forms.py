from django.contrib.auth.forms import UserCreationForm
from .models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        Model = User
        fields = ['username', 'password',]