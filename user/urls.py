from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser().as_view(), name='register-user'),
    path('auth/', views.AuthUser().as_view(), name='auth-user'),
    path('logout/', views.Logout().as_view(), name='logout-user')
]
