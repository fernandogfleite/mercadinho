from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos import views
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'car', views.CarViewSet)
router.register(r'carindentify', views.IndentifyCarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]