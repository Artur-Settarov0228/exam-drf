from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorProfileView


urlpatterns = [
    path("doctors/", DoctorListView.as_view()),
    path("doctor/profile/", DoctorProfileView.as_view()),
    path("doctors/<int:docdor_id>/", DoctorDetailView.as_view()),
]