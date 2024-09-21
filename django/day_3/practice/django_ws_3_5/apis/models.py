from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator


class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[MinLengthValidator(15,'15글자 이상 입력해야합니다.'),MaxLengthValidator(60,'60글자 이하로 입력해야 합니다.'),URLValidator()])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(default=None,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
