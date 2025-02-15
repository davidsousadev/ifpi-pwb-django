from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Franquia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    franquia = models.ForeignKey(Franquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.CharField(max_length=255)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.produto.quantidade < self.quantidade:
            raise ValueError("Estoque insuficiente para a venda.")
        self.produto.quantidade -= self.quantidade
        self.produto.save()
        self.valor_total = self.quantidade * self.produto.preco
        super().save(*args, **kwargs)
