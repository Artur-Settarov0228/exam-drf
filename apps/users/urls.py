from django.urls import path
from .views import RegisterView, LoginView, MeView, UserListView, UserDeatilView, UserDeleteView, ProfilePatentView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),

    path('users/', UserListView.as_view()),
    path('users/<int:user_id>/', UserDeatilView.as_view()),
    path('users/<int:user_id>/delete/', UserDeleteView.as_view()),
    
    path('profiles/patient/<int:user_id>/', ProfilePatentView.as_view())
 
    
    ]