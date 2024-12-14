from rest_framework import serializers
from .models import Article

# serializer == 어떤 곳에서도 활용이 가능하도록 정보를 가공하는 과정

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content',)
        

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'