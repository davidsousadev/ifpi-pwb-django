from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Gestão de Projeto'
admin.site.index_title = 'Cadastros e Consultas'

urlpatterns = [
    path('admin/', admin.site.urls),
]
