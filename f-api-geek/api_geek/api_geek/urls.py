from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="API GEEK",
        default_version='v1',
        description="API de vendas de artigos geek",
    ),
    public=True,
    permission_classes=[AllowAny],
)

admin.site.site_header = 'F-API-GEEK'
admin.site.index_title = 'Administração da API GEEK'
admin.site.site_title = 'F-API-GEEK'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendas.urls')), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
