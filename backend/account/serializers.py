from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, StudentProfile
from phonenumber_field.serializerfields import PhoneNumberField

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        token['email'] = user.email
        return token

class UserSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region='EG')
    is_verified = serializers.BooleanField(read_only=True)  # Added read-only

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'user_type', 'is_verified')

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = StudentProfile
        fields = ('user', 'full_name', 'date_of_birth')  # Replaced __all__ with explicit fields

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = PhoneNumberField(region='EG', required=True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'user_type')

    def validate_user_type(self, value):  # New validation
        if value not in dict(User.USER_TYPES).keys():
            raise serializers.ValidationError("Invalid user type. Must be ADMIN or STUDENT")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            user_type=validated_data.get('user_type', 'STUDENT')
        )
        return user