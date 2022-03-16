from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, required=True)
    password = serializers.CharField(
        required=True,
        style={"input_type": "password", },
        write_only=True,

    )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        min_length=4,
        max_length=255,
        validators=[UniqueValidator(
            queryset=User.objects.all(), message='Email is already Taken',)])

    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }


class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    otp_code = serializers.CharField(max_length=6, required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, required=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, required=True)
    password = serializers.CharField(
        max_length=200,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    otp_code = serializers.CharField(max_length=6, required=True)


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, required=True)
    old_password = serializers.CharField(
        max_length=200,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    new_password = serializers.CharField(
        max_length=200,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
