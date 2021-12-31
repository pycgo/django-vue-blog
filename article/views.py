from article.models import Article,Category,Tag,Avatar
from article.permissions import IsAdminUserOrReadOnly

from rest_framework import viewsets,filters
from article.serializers import ArticleSerializer,ArticleDetailSerializer,AvatarSerializer
from article.serializers import CategorySerializer
from article.serializers import TagSerializer

# 文章标签
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    #精确检索
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['author__username']
    #模糊检索
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # filterset_class = ArticleTitleFilter


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]