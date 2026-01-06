from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import CustomUser, ProfilePatient
from apps.doctors.models import ProfileDoctor


@receiver(post_save, sender=CustomUser)
def create_profiles(sender, instance, created, **kwargs):
    if not created:
        return


    if instance.role == CustomUser.Role.DOCTOR:
        ProfileDoctor.objects.create(
            user=instance,
            specialization="Unknown",
            experience_years=0,
            gender="male",
        )


    elif instance.role == CustomUser.Role.PATIENT:
        ProfilePatient.objects.create(
            user=instance,
            phone="",
            date_of_birth="2000-01-01",
            gender="male",
        )
