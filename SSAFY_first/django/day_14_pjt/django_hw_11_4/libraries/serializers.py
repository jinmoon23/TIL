from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
    class ReviewsSerializer(serializers.ModelSerializer):
        class Meta():
            model = Review
            fields = ['content','score',]
    review_set = ReviewsSerializer(many=True,read_only=True)
    review_count = serializers.IntegerField(source='review_set.count',read_only=True)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)
    class BookIsbnSerializer(serializers.ModelSerializer):
        class Meta():
            model = Book
            fields = ['isbn']
    book = BookIsbnSerializer(read_only=True)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)