from django.db import models
from apps.users.models import ProfilePatient
from apps.doctors.models import ProfileDoctor


class TimeSlot(models.Model):
    doctor = models.ForeignKey(
        ProfileDoctor,
        on_delete=models.CASCADE,
        related_name='time_slot'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} | {self.date} {self.start_time}-{self.end_time}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(ProfileDoctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey( ProfilePatient, on_delete=models.CASCADE, related_name='appointments')
    timeslot = models.OneToOneField( TimeSlot, on_delete=models.CASCADE, related_name='appointment')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.status})"
