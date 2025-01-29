from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
      model = get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
   class Meta(UserChangeForm.Meta):
      # 어떻게하지? 일단 어떻게 뜨는지 보자
      model = get_user_model()
      # 쓸데없는 수정 폼이 많이 뜸
      # 특정한 부분만 받도록 하자
      fields = ['first_name','last_name',]