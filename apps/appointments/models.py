from django.db import models
from apps.users.models import ProfilePatient
from apps.doctors.models import ProfileDoctor, TimeSlotDoctor



class Appointment(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(ProfileDoctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey( ProfilePatient, on_delete=models.CASCADE, related_name='appointments')
    timeslot = models.OneToOneField( TimeSlotDoctor, on_delete=models.CASCADE, related_name='appointment')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.status})"
