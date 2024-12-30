from rest_framework import viewsets, permissions
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        author_id = self.request.query_params.get('author')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer