from rest_framework import viewsets
from complex_design_backend_rest_api.serializers import PostSerializer
from complex_design_backend.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer