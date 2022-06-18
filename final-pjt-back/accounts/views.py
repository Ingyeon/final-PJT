from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
# Create your views here.

@api_view(['GET'])
def user_profile(request,username):
    user = get_object_or_404(get_user_model(),username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request,user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user # 로그인 유저가 되어야함.
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            # 언팔로우
            you.followers.remove(me)
        else:
            # 팔로우
            you.followers.add(me)
    serializer = ProfileSerializer(you)
    return Response(serializer.data)