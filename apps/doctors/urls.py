from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorProfileView


urlpatterns = [
    path("doctors/", DoctorListView.as_view()),
    path("doctor/profile/", DoctorProfileView.as_view()),
    path("doctors/<int:doctor_id>/", DoctorDetailView.as_view()),
]