from rest_framework import serializers
from apps.doctors.models import TimeSlotDoctor
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def validate_timeslot(self, value):
    
        if not TimeSlotDoctor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError(
                "Bunday time slot mavjud emas"
            )
        return value
