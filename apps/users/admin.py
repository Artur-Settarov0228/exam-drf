from django.contrib import admin

from .models import CustomUser, ProfilePatient

admin.site.register(CustomUser)
admin.site.register(ProfilePatient)