from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views

# Criando um roteador para a API
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Inclui as rotas da API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Rotas de autenticação
]
