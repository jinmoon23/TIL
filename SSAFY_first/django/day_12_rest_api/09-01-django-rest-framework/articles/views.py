from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework import status

# 해당 데코레이터를 사용하지 않으면 오류가 발생함 -> 필수!!
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        # 타입: 쿼리셋 -> 쿼리셋은 장고에서만 사용하는 데이터타입
        articles = Article.objects.all()
        # 어디서든 사용할 수 있도록 직렬화 과정이 필요함 / articles(data)가 쿼리셋일 경우 many=True 필요
        serializer = ArticleListSerializer(articles, many=True)
        # 실제 데이터 만! 응답해야 한다~!
        return Response(serializer.data)
    elif request.method == 'POST' :
        # 기존에는 request.POST 임! 문법에 차이가 있음을 확인하자
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 저장 성공 후 201 상태 코드 반환
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 후 400 상태 코드 반환
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 직렬화 진행
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # partial -> 부분 업데이트를 허용하도록 하는 인자
        # instance가 필요 없다!
        serializer = ArticleSerializer(article,data=request.data,partial=True)
        # raize_exception=True 하면 가장 아래의 코드를 안 적어도 됨!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
