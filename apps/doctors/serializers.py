from rest_framework import serializers
from .models import ProfileDoctor, TimeSlotDoctor
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = (
            "password",
            "is_staff",
            "is_superuser",
        )


class DoctorListDetailSeralizer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = ProfileDoctor
        fields = (
            "id",
            "specialization",
            "experience_years",
            "gender",
            "user",
        )


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDoctor
        fields = (
            "specialization",
            "experience_years",
            "gender",
        )

class TimeSlotDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotDoctor
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_time'] >= attrs['end_time']:
            raise serializers.ValidationError("Start time must be before end time.")
        return attrs
    