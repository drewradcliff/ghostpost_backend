
from homepage.models import Post
from homepage.serializers import PostSerializer

from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-submission_date')
    serializer_class = PostSerializer