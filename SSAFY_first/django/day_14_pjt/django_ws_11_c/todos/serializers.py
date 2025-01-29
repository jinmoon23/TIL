from rest_framework import serializers
from .models import Todo
from .models import Recommend

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    class RecommendSerializerForTodoDetail(serializers.ModelSerializer):
        class Meta():
            model = Recommend
            exclude = ['todo',]
    recommend_set = RecommendSerializerForTodoDetail(many=True,read_only=True)

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )

class RecommendSerializer(serializers.ModelSerializer):
    class Meta():
        model = Recommend
        fields = '__all__'
        # 읽기 전용으로 설정
        read_only_fields = ['todo',]