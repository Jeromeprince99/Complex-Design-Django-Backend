from rest_framework import serializers
from complex_design_backend.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','image','content','time','video')