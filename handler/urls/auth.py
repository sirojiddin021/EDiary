from django.urls import path
import handler.views as views

auth_urls = [
    path('auth/register/', views.RegisterAPIView.as_view()),
    path('auth/login/', views.TokenObtainPairView.as_view()),
    path('auth/profile/', views.ProfileAPIView.as_view()),
]
