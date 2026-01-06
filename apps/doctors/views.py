from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import ProfileDoctor
from .serializers import  DoctorListDetailSeralizer, DoctorUpdateSerializer

from apps.users.permissions import IsDoctor, IsOwner, IsAdmin



class DoctorListView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request) -> Response:
        doctors = ProfileDoctor.objects.all()
        serializer = DoctorListDetailSeralizer(doctors, many=True)

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


