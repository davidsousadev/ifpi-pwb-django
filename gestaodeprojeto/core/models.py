import datetime
from django.db import models


# Status de Projeto (exemplo)
STATUS_CHOICES = (
    ('P', 'Planejamento'),
    ('E', 'Em Execução'),
    ('F', 'Finalizado'),
)

# Modelo Projeto
class Projeto(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=128, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    data_criacao = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)
    data_conclusao = models.DateTimeField(verbose_name='Data de Conclusão', null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P', verbose_name='Status')
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='projetos')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome

    @property
    def tempo_execucao(self):
        if self.data_conclusao:
            return (self.data_conclusao - self.data_criacao).days
        return None


# Modelo Equipe
class Equipe(models.Model):
    nome = models.CharField(verbose_name='Nome da Equipe', max_length=128, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    data_criacao = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    @property
    def count_projetos(self):
        return self.projetos.count()


# Modelo Membro
class Membro(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=128, blank=False, null=False)
    cargo = models.CharField(verbose_name='Cargo', max_length=64, blank=False, null=False)
    email = models.EmailField(verbose_name='E-mail', unique=True, blank=False, null=False)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='membros')
    data_entrada = models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.cargo})'

    @property
    def tempo_equipe(self):
        return (datetime.date.today() - self.data_entrada.date()).days


# Modelo Atividade
class Atividade(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=128, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    data_inicio = models.DateTimeField(verbose_name='Data de Início', blank=False, null=False)
    data_conclusao = models.DateTimeField(verbose_name='Data de Conclusão', null=True, blank=True)
    membro = models.ForeignKey('Membro', on_delete=models.CASCADE, related_name='atividades')
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='atividades')

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['data_inicio']

    def __str__(self):
        return self.nome

    @property
    def duracao(self):
        if self.data_conclusao:
            return (self.data_conclusao - self.data_inicio).days
        return None
