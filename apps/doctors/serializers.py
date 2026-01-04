from rest_framework import serializers
from .models import ProfileDoctor
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = (
            "password",
            "is_staff",
            "is_superuser",
        )



class DoctorListDetailSeralizer(serializers.Serializer):
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
        fields = ('specialization", "experience_years", "gender')
