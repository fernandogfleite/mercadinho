from rest_framework import serializers
from produtos.models import Product, Category, ShoppingCar, IndentifyShoppingCar
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Product
        fields = ['url','id', 'name', 'description', 'id_category', 'category','price']
        read_only_fields = ['category']
        extra_kwargs = {
            'id_category' : {'write_only':True}
        }
      

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'products']

class ShoppingCarSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = ShoppingCar
        fields = ['url', 'id', 'status', 'products']

class IndentifyShoppingCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndentifyShoppingCar
        fields = ['url', 'shoppingcar', 'product', 'quantity']
