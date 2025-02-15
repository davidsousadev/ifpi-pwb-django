from rest_framework import serializers
from .models import Produto, Categoria, Franquia, Venda

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class FranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franquia
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
