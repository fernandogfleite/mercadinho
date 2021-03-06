from produtos.models import Product, Category, IndentifyShoppingCar, ShoppingCar
from produtos.serializers import ProductSerializer, UserSerializer, CategorySerializer, ShoppingCarSerializer, IndentifyShoppingCarSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name','description', 'id_category']
    search_fields = ['^name','description', 'id_category']

    def perform_create(self, serializer):
        

        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ShoppingCarViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCar.objects.all()
    serializer_class = ShoppingCarSerializer
    permission_classes = [IsAuthenticated]

class IndentifyShoppingCarViewSet(viewsets.ModelViewSet):
    queryset = IndentifyShoppingCar.objects.all()
    serializer_class = IndentifyShoppingCarSerializer
    permission_classes = [IsAuthenticated]