from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from apps.filme.views import FilmeViewSet, CategoriaViewSet, CreateUser
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



# criando o router
router = routers.DefaultRouter()

router.register('filmes', FilmeViewSet, basename="Filmes")
router.register('categorias', CategoriaViewSet, basename="Categorias")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('apps.filme.urls')),
    path('generate-token/', views.obtain_auth_token),
    path('cadastro/', CreateUser.as_view(), name='create_user'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
