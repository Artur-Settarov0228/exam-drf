from django.db import models
from apps.users.models import CustomUser

class ProfileDoctor(models.Model):
    
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )
    specialization = models.CharField(max_length=120)
    experience_years = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"
    

class TimeSlotDoctor(models.Model):
    doctor = models.ForeignKey(ProfileDoctor, on_delete=models.CASCADE, related_name="doctor_profile")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_aviable = models.BooleanField()
