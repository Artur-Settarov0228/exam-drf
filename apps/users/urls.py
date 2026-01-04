from django.urls import path
from .views import RegisterView, LoginView, MeView, UserListView, UserDeatilView, UserDeleteView, ProfilePatentView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me/', MeView.as_view()),

    path('uauth/sers/', UserListView.as_view()),
    path('auth/users/<int:user_id>/', UserDeatilView.as_view()),
    path('auth/users/<int:user_id>/delete/', UserDeleteView.as_view()),

    path('auth/profiles/patient/<int:user_id>/', ProfilePatentView.as_view())
 
    
    ]