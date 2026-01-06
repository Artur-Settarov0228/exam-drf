from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorProfileView, TimeSlotsView, TimeSlotDoctor, TimeSlotCreateView, TimeSlotDetailView


urlpatterns = [
    path("doctors/", DoctorListView.as_view()),
    path("doctor/profile/", DoctorProfileView.as_view()),
    path("doctors/<int:doctor_id>/", DoctorDetailView.as_view()),
    path("doctors/<int:doctor_id>/time-lots/", TimeSlotsView.as_view()),
    
    path('timeslots/',TimeSlotCreateView.as_view(), name="timeslots_view" ),
    path('timeslots/<int:slot_id>/', TimeSlotDetailView.as_view(), name = "timeslot_detail")




    
]