from django.urls import path
from .views import AppointmentCreateView

urlpatterns = [
    path("appointments/create/", AppointmentCreateView.as_view(), name="appointment_create"),
]
