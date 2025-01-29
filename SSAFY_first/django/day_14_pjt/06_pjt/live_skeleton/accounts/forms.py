from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CustomUserCreationsForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model을 제외하고는 모두 상속받아서 사용하면 됨!
        model = get_user_model()
        