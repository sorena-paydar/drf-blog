from django.urls import path
from .views import BlogPostListView, BlogPostDetailView

urlpatterns = [
    path("", BlogPostListView.as_view(), name="blog_posts"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="blog_post_detail"),
]
