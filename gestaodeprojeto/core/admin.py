from django.contrib import admin
from .models import Projeto, Equipe, Membro, Atividade

# Inline para Atividades no Admin de Projeto
class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1  # Número de atividades em branco para adicionar
    fields = ('nome', 'descricao', 'data_inicio', 'data_conclusao', 'membro')

# Inline para Membros no Admin de Equipe
class MembroInline(admin.TabularInline):
    model = Membro
    extra = 1  # Número de membros em branco para adicionar
    fields = ('nome', 'cargo', 'email', 'ativo')

# Admin para o modelo Projeto
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status', 'data_criacao', 'data_conclusao', 'equipe', 'tempo_execucao')
    search_fields = ('nome', 'descricao', 'equipe__nome')
    list_filter = ('status', 'equipe')
    inlines = [AtividadeInline]

    def tempo_execucao(self, obj):
        return obj.tempo_execucao if obj.tempo_execucao else 'Não concluído'
    tempo_execucao.short_description = 'Tempo de Execução (dias)'

# Admin para o modelo Equipe
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao', 'count_projetos')
    search_fields = ('nome',)
    inlines = [MembroInline]

    def count_projetos(self, obj):
        return obj.count_projetos
    count_projetos.short_description = 'Qtd Projetos'

# Admin para o modelo Membro
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'email', 'equipe', 'ativo', 'tempo_equipe')
    search_fields = ('nome', 'cargo', 'email', 'equipe__nome')
    list_filter = ('equipe', 'ativo')

    def tempo_equipe(self, obj):
        return obj.tempo_equipe
    tempo_equipe.short_description = 'Tempo na Equipe (dias)'

# Admin para o modelo Atividade
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicio', 'data_conclusao', 'membro', 'projeto', 'duracao')
    search_fields = ('nome', 'descricao', 'membro__nome', 'projeto__nome')
    list_filter = ('membro', 'projeto')

    def duracao(self, obj):
        return obj.duracao if obj.duracao else 'Não concluída'
    duracao.short_description = 'Duração (dias)'

# Registro dos modelos com suas configurações de admin
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(Atividade, AtividadeAdmin)
