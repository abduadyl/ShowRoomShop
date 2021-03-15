from rest_framework import viewsets, generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .permissions import IsAuthorPermission


class CartListView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthorPermission, ]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthorPermission, ]


