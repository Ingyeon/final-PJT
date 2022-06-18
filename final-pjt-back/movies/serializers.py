from rest_framework import serializers
from .models import Movie,Similar

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class SimilarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Similar
        fields = '__all__'

