from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Review,Comment,Movie
from .serializers.comment import CommentSerializer
from .serializers.review import ReviewListSerializer,ReviewSerializer

# 리뷰리스트 가져오기
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.annotate(
        comment_count = Count('comments', distinct=True),
        like_count = Count('like_users', distinct=True)).order_by('-pk')
    serializer = ReviewListSerializer(reviews,many=True)
    return Response(serializer.data)

# 리뷰 생성
@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)


# 리뷰 상세 정보 및 수정, 삭제 
@api_view(['GET','PUT','DELETE'])
def review_detail_or_update_or_delete(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        print(request.data)
        if request.user == review.user:
            serializer = ReviewSerializer(data=request.data, instance=review)
            print(serializer.instance.content)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    
    # 이미 리뷰 좋아요 했다면 좋아요 삭제 구현
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    # 안했다면 좋아요
    else:
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


# 아래부터는 댓글 구현 

#댓글 생성 관리
@api_view(['POST'])
def create_comment(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
