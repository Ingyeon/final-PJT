from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk', 'title', 'content')
            
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'followings')
    
    like_reviews = ReviewSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    followers = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_reviews', 'reviews','followers','followings')

