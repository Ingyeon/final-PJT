from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review
from .comment import CommentSerializer
# from movies.serializers import MovieSerializer

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    
    # 글쓴이 확인
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'comments', 'rank', 'like_users', 'movie','movie_title','poster_path')
        # review 작동 하기 위해 rank필드 제외함


# 글 목록 불러오는 serializer
class ReviewListSerializer(serializers.ModelSerializer):
    # 글쓴이 확인
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    
    # 쿼리셋 데이터 정리용(annotate) -> view에서 받아옵니다.
    # 댓글 갯수 및 좋아요 갯수 확인용도
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count','movie','movie_title')