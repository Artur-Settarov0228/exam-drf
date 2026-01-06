
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.doctors.models import TimeSlotDoctor
from .models import Appointment
from .serializers import AppointmentSerializer
from apps.users.permissions import IsPatient


class AppointmentCreateView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def post(self, request):
        timeslot_id = request.data.get("timeslot")

    
        timeslot = get_object_or_404(TimeSlotDoctor, id=timeslot_id)
        serializer = AppointmentSerializer(
            data={
                "timeslot": timeslot.id,
                "patient": request.user.id
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
