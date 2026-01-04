from django.shortcuts import get_object_or_404


from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, MeSerializer, UserDeteilSerializer, UserListSerializer, UserUpdateSerializer, UserSerializer
from .models import CustomUser, ProfilePatient
from .permissions import IsAdmin,  IsPatient


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User muvaffaqiyatli ro'yxatdan o'tdi",
                "user": UserRegisterSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserRegisterSerializer(user).data
            })
        return Response(
            {"error": "Login yoki parol notogri"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = CustomUser.objects.filter(role=CustomUser.Role.PATIENT)
        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)


class UserDeatilView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(CustomUser, user_id=user_id)
        serializer = UserDeteilSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(CustomUser, user_id=user_id)
        serializer = UserDeteilSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()

        return Response(
            {"detail": f"{user_id} - user muvaffaqiyatli ochirildi"},
            status=status.HTTP_200_OK,
        )

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = MeSerializer(request.user)
        return Response(serializer.data)
    

class ProfilePatentView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]
    def get(self, request, user_id):
        profile = get_object_or_404(ProfilePatient, user_id = user_id)
        serializer = UserSerializer(profile)
        return Response(serializer.data)
    
    def patch(self, request, user_id):
        profile = get_object_or_404(ProfilePatient, user_id = user_id)
        serializer = UserUpdateSerializer(profile, data = request.data , partail = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
