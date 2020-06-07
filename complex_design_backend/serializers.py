from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
