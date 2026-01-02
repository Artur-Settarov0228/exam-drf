from django.contrib.auth.models import AbstractUser

from django.db import models

class CostumUser(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'admin'
        DOCTOR = "DOCTOR", 'doctor'
        PATIENT = "PATIENT", 'patient'
    
    role = models.CharField(
            max_length=15,
            choices = Role.choices,
            default = Role.PATIENT
        )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

