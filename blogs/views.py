from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated


class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
