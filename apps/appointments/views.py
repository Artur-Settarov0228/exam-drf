
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.doctors.models import TimeSlotDoctor
from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentStatusSerializer
from apps.users.permissions import IsPatient, IsAdmin, IsOwner, IsDoctor


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

class MyAppointmentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_doctor:
            qs = Appointment.objects.filter(
                timeslot__doctor__user=request.user
            )
        else:
            qs = Appointment.objects.filter(patient=request.user)

        serializer = AppointmentSerializer(qs, many=True)
        return Response(serializer.data)


class AppointmentListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        qs = Appointment.objects.all()
        serializer = AppointmentSerializer(qs, many=True)
        return Response(serializer.data)


class AppointmentDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

    def get(self, request, id):
        appointment = get_object_or_404(Appointment, id=id)
        self.check_object_permissions(request, appointment)

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

class AppointmentStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor | IsAdmin]

    def patch(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)

        serializer = AppointmentStatusSerializer(
            appointment,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class AppointmentDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

    def delete(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        self.check_object_permissions(request, appointment)

        appointment.delete()
        return Response(
            {"detail": "Appointment bekor qilindi"},
            status=status.HTTP_204_NO_CONTENT
        )
