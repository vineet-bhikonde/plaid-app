from knox import views as knox_views
from .views import LoginApiView, RegisterAPIView, UserApiView
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='registration'),
    path('api/user', UserApiView.as_view(), name='user'),
    path('api/login/', LoginApiView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]
