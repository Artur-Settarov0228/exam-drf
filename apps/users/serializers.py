from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from apps.users.models import CustomUser, ProfilePatient
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "groups",
            "user_permissions",
            "is_staff",
            "last_login",
            "is_active",
        ]

class UserRegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username',
                  'email', 
                  'password', 
                  'confirm_password', 
                  'role', 
                  'first_name', 
                  'last_name'
        ]
 
    def validate(self, attrs):
        role = attrs.get('role', User.Role.PATIENT)
        if role == User.Role.ADMIN:
            raise serializers.ValidationError("Admin register qilolmaysiz")
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password va confirm_password mos kelmadi"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')  
        password = validated_data.pop('password')
    

        user = User(**validated_data)
        user.set_password(password)  
    
        user.save()
        return user
    
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )

class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username', read_only = True)
    email = serializers.EmailField(source = 'user.email', read_only = True)
    last_name = serializers.CharField(source = 'user.last_name', read_only = True)
    first_name = serializers.CharField(source = 'user.first_name', read_only = True)
   
   
    class Meta:
        model = ProfilePatient
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "date_of_birth",
            "gender"
        )


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "is_active",
            "created_at",
        )

class UserDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "role",
            "is_active"
        )
