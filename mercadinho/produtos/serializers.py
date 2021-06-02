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
        fields = ['url','id', 'name', 'description', 'price','id_category', 'category']
        read_only_fields = ['category']
        extra_kwargs = {
            'id_category' : {'write_only':True}
        }
      

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'products']

class ProductNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class IndentifyShoppingCarSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = IndentifyShoppingCar
        fields = ['url', 'shoppingcar','product', 'price','quantity', 'total_price']
        read_only_fields = ('price',)
        extra_kwargs = {
            'shoppingcar' : {'write_only':True}
        }

class ShoppingCarSerializer(serializers.ModelSerializer):
    products = IndentifyShoppingCarSerializer(read_only=True,many=True)
    class Meta:
        model = ShoppingCar
        fields = ['url', 'id', 'status', 'products', 'shoppingcar_totalprice']