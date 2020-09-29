
from homepage.models import Post
from homepage.serializers import PostSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-submission_date')
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def add_upvote(self, request, pk=None):
        post = self.get_object()
        post.up_votes += 1
        post.score = post.up_votes - post.down_votes
        post.save()
        return Response({'status': 'post upvoted'})

    @action(detail=True, methods=['post'])
    def add_downvote(self, request, pk=None):
        post = self.get_object()
        post.down_votes += 1
        post.score = post.up_votes - post.down_votes
        post.save()
        return Response({'status': 'post downvoted'})