from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Produto, Categoria, Franquia, Venda
from .serializers import ProdutoSerializer, CategoriaSerializer, FranquiaSerializer, VendaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FranquiaViewSet(viewsets.ModelViewSet):
    queryset = Franquia.objects.all()
    serializer_class = FranquiaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['post'])
    def repor_estoque(self, request, pk=None):
        produto = self.get_object()
        quantidade = int(request.data.get('quantidade', 0))
        if quantidade > 0:
            produto.quantidade += quantidade
            produto.save()
            return Response({'status': 'estoque atualizado'}, status=status.HTTP_200_OK)
        return Response({'error': 'Quantidade inválida'}, status=status.HTTP_400_BAD_REQUEST)



class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            produto = Produto.objects.get(id=request.data['produto'])
            quantidade_venda = int(request.data['quantidade'])

            if produto.quantidade < quantidade_venda:
                return Response({'error': 'Estoque insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

            # Atualizando o estoque após a venda
            produto.quantidade -= quantidade_venda
            produto.save()

            # Criando a venda
            venda = Venda.objects.create(
                cliente=request.data['cliente'],
                produto=produto,
                quantidade=quantidade_venda,
                valor_venda=produto.preco * quantidade_venda,
                data_venda=request.data['data_venda']
            )

            return Response({
                'status': 'Venda realizada com sucesso',
                'venda_id': venda.id,
                'produto': produto.nome,
                'quantidade': quantidade_venda,
                'total_venda': venda.valor_venda
            }, status=status.HTTP_201_CREATED)
        
        except Produto.DoesNotExist:
            return Response({'error': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Dados incompletos'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
