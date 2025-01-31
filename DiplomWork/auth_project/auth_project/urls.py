"""
URL configuration for auth_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from auth_app import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout_session/', views.logout_session, name='logout_session'),
    path('session_register/', views.session_register, name='session_register'),
    path('session_login/', views.session_login, name='session_login'),
    path('secure_page_session/', views.secure_page_session, name='secure_page_session'),
    path('oauth_login/', views.oauth_login, name='oauth_login'),
    path('accounts/', include('allauth.urls')),  # Для маршрутов allauth
    path('secure_page/', views.secure_page_session, name='secure_page'),
    path('logout_oauth/', views.logout_oauth, name='logout_oauth'),
    path('jwt_login/', views.jwt_login, name='jwt_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwt/register/', views.jwt_register, name='jwt_register'),
    path('secure_page_jwt/', views.secure_page_jwt, name='secure_page_jwt'),
    path('logout_jwt/', views.logout_jwt, name='logout_jwt'),
]
