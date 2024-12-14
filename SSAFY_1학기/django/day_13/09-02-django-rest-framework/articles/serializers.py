from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    # Nested relationships
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
    # comment_set 오버라이드
    # 유효성 검사의 대상이 아니기 때문에 read_only 옵션인자 필요
    # article에 대해 comments는 항상 N이기 때문에 many 옵션인자도 필요
    # 이거 comment_set 말고 다른 변수명 안됨!!
    comment_set = CommentDetailSerializer(read_only=True,many=True)
    # 댓글 개수도 보여줄래! 오버라이드 아님!
    # 여기서는 comment_count 이거 다른 변수명 써도 괜찮음!
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    # 댓글 조회 시 게시글 출력 내용을 변경하기 위한 오버라이딩
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ['title',]
    # 그런데 기존 fields를 오버라이드 하게 되면 아래의 read_only fields를 사용할 수 없게됨
    # 그럼 어떻게 해?
    # 다른 방법을 활용해야지!
    # 모델 시리얼라이저의 read_only 인자를 설정해줘야 한다.
    article = ArticleTitleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        # 1. foreignKey 데이터는 유효성 검사에서는 제외하고 싶고
        # 2. 결과 데이터에는 포함하고 싶음
        fields = '__all__'
        # 3. 그런 데이터를 읽기 전용 필드라고 부르고 아래의 코드로 해결한다.
        read_only_fields = ['article',]
        # 이런식으로 작성하면 오류 발생!
        # exclude = ['article']
