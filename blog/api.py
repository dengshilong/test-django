from rest_framework import generics
from .serializer import PostSerializer
from .models import Post


class PostListAPI(generics.ListAPIView):
    serializer_class = PostSerializer
    model = Post
    paginate_by = 10


    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publish_time')
        queryset = queryset.select_related('category')
        queryset = queryset.prefetch_related('tag')
        return queryset
