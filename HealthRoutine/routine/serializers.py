from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'sports_name', 'routine', 'sets', 'created_date', 'updated_date')
