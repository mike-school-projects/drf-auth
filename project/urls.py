from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/app/', include('app.urls')),
    path('api-auth', include("rest_framework.urls")),
    path('', lambda req: redirect('api/v1/app/')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
