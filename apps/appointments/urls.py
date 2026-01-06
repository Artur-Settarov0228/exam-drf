from django.urls import path
from .views import AppointmentCreateView, MyAppointmentsView, AppointmentListView, AppointmentDetailView, AppointmentStatusUpdateView, AppointmentDeleteView    

urlpatterns = [
    path("appointments/create/", AppointmentCreateView.as_view(), name="appointment_create"),
    path("appointments/me/", MyAppointmentsView.as_view()),
    path("appointments/all/", AppointmentListView.as_view()),
    path("appointments/<int:pk>/", AppointmentDetailView.as_view()),
    path("appointments/<int:pk>/status/", AppointmentStatusUpdateView.as_view()),
    path("appointments/<int:pk>/delete/", AppointmentDeleteView.as_view()),
]
