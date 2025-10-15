from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostSerializer
# Create your views here.
class PostListApi(generics.ListCreateAPIView):
	permission_class = [permissions.IsAuthenticatedOrReadOnly,]
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
	permission_class = [permissions.IsAuthenticatedOrReadOnly,]
	queryset = Post.objects.all()
	serializer_class = PostSerializer