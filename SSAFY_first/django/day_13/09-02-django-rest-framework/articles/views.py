from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk) 이 코드를 아래의 코드로 변경!
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 조회 함수        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    # 시리얼라이저 진행
    # 쿼리셋인 경우 넣어줘야 하는 옵션인자 many!
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_one(request,comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # (기존 데이터, 사용자가 수정한 데이터)
        serializer = CommentSerializer(comment,request.data)
        if serializer.is_valid(raise_exception=True):
            # 생성과 달리 article을 넣음으로써 foreignKey 인입이 필요하지 않다.
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def comment_create(request,article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article,pk=article_pk)
    # 조회와 다른점! 인자 주의
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # foreignKey를 아래의 방식으로 넣어준다!
        serializer.save(article=article)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
