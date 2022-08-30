from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
