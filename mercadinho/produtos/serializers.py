from rest_framework import serializers
from produtos.models import Produto, Categoria, Car, IndentifyCar
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ['id', 'name']

class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produto
        fields = ['url','id', 'name', 'description', 'id_category', 'category','value']
        read_only_fields = ['category']
        extra_kwargs = {
            'id_category' : {'write_only':True}
        }
      

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'produtos']

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ['url', 'id', 'status']

class IndentifyCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndentifyCar
        fields = ['url', 'carrinho', 'produto', 'quantidade']
