from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import ProfileDoctor, TimeSlotDoctor
from .serializers import  DoctorListDetailSeralizer, DoctorUpdateSerializer, TimeSlotDoctorSerializer

from apps.users.permissions import IsDoctor, IsOwner, IsAdmin, IsPatient



class DoctorListView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request) -> Response:
        doctors = ProfileDoctor.objects.all()
        serializer = DoctorListDetailSeralizer(doctors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class TimeSlotsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsPatient]

    def get(self, request:Request, doctor_id:int):
        doctor = ProfileDoctor.objects.get(id = doctor_id)
        time_slots = TimeSlotDoctor.objects.filter(doctor=doctor)
        serializer = TimeSlotDoctorSerializer(time_slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated,IsOwner ]

    def get(self, request: Request, doctor_id: int):
        doctor = get_object_or_404(ProfileDoctor, id=doctor_id)
        serializer = DoctorListDetailSeralizer(doctor)

        return Response(serializer.data, status = status.HTTP_200_OK)
    


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request: Request) -> Response:
        profile = get_object_or_404(ProfileDoctor, user=request.user)
        serializer = DoctorListDetailSeralizer(profile)

        return Response(serializer.data)

    def patch(self, request: Request):
        profile = get_object_or_404(ProfileDoctor, user=request.user)
        serializer = DoctorUpdateSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TimeSlotCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsDoctor]
    def get(self, request:Request):
        timeslots = TimeSlotDoctor.objects.filter(doctor = request.user.doctor_profile)
        serializer = TimeSlotDoctorSerializer(timeslots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request:Request):
        doctor = ProfileDoctor.objects.filter(user=request.user).first()
        data = request.data.copy()
        data['doctor'] = doctor.id
        serializer = TimeSlotDoctorSerializer(data=data, context={'request': request} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




class TimeSlotDetailView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request:Request, slot_id:int):
        timeslot = get_object_or_404(TimeSlotDoctor, id = slot_id, doctor = request.user.doctor_profile)
        serializer = TimeSlotDoctorSerializer(timeslot)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request:Request, slot_id:int):
        timeslot = get_object_or_404(TimeSlotDoctor, id = slot_id, doctor = request.user.doctor_profile)
        if not timeslot.is_available:
            raise ValidationError(
                "Band qilinib bulgan TimeSlotni o'chirish mumkin emas"
            )
        timeslot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        