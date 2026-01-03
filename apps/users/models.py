from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        DOCTOR = 'doctor', 'Doctor'
        PATIENT = 'patient', 'Patient'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_admin(self) -> bool:
        return self.role == self.Role.ADMIN

    @property
    def is_doctor(self) -> bool:
        return self.role == self.Role.DOCTOR

    @property
    def is_patient(self) -> bool:
        return self.role == self.Role.PATIENT


class PatientProfile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    user = models.OneToOneField(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} (Patient)"