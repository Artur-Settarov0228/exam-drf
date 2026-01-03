from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confrim_password = serializers.CharField(write_only = True, required = True)
    role = serializers.ChoiceField(choices= User.Role.choices, required = True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confrim_passqoed', 'role' )

        def vailidate(self, attrs):
            if attrs['password'] != attrs['confrim_password']:
                raise serializers.ValidationError({"parol":"parollar bir birga tugri kemadi qaytadan urinib kuring"})
            
            if attrs['role'] == User.Role.ADMIN:
                raise serializers.ValidationError({"role": "siz admin bulib ruyhatdan utaolamysiz"})
            
            return attrs
        def create(self, validated_data):
            validated_data.pop('confirim_password')
            password = validated_data.pop('password')
            role = validated_data.pop('role')


            user = User(**validated_data)
            user.set_password('password')
            user.role = role
            
            user.save()

            return user
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'created_at']

