from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .permissions import IsAuthorPermission, IsDesignerPermission, IsCustomerPermission


class PaginationProduct(PageNumberPagination):
    page_size = 5

class PaginationReview(PageNumberPagination):
    page_size = 10


class PermissionMixinProduct:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsDesignerPermission, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = [AllowAny, ]
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

class PermissionMixinReview:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsCustomerPermission, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = [AllowAny, ]
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


class ProductViewSet(PermissionMixinProduct, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationProduct

    @action(detail=True, methods=['post'])
    def like(self):
        pass

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewViewSet(PermissionMixinReview, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PaginationReview





