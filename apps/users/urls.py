
from django.urls import path
from .views import RegisterView, MeView, UserListView, UserDeatilView, UserDeleteView, ProfilePatientView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me/', MeView.as_view()),

    path('auth/user/', UserListView.as_view()),
    path('auth/users/<int:user_id>/', UserDeatilView.as_view()),
    path('auth/users/<int:user_id>/delete/', UserDeleteView.as_view()),


     path("patient/profiles/", ProfilePatientView.as_view(), name="patient_profile"),
 
    
    ]