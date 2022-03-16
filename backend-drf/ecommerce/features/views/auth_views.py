from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token          # DRF Token
from rest_framework_simplejwt.tokens import RefreshToken  # JWT  Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.views import APIView
from features.serializers.auth_serializers import (
    LoginSerializer, RegisterSerializer, VerifyOtpSerializer,
    ForgotPasswordSerializer, ResetPasswordSerializer, ChangePasswordSerializer)
import random


from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if not user.is_verified:
                    return Response({'verification': False}, status=status.HTTP_400_BAD_REQUEST)
                if user.check_password(password) is not True:
                    return Response({'error': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
                if user.check_password(password) and user.is_verified:
                    # token, created = Token.objects.get_or_create(user=user)  # DRF Token
                    jwt_user_token = get_tokens_for_user(user)
                    print(jwt_user_token)
                    # return Response({'email': email, 'token': token.key, }, status=status.HTTP_200_OK) # DRF TOKEN
                    # JWT TOKEN
                    return Response({'email': email, 'token': jwt_user_token, }, status=status.HTTP_200_OK)
            except Exception as err:
                return Response({'msg': str(err)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'success': "Successfully Logged out"}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                first_name = serializer.validated_data['first_name']
                last_name = serializer.validated_data['last_name']
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
            except Exception as err:
                return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
            otp_code = str(random.randint(100000, 1000000))
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                otp_code=otp_code
            )
            user.set_password(password)
            user.save()

            verification_link = 'http://127.0.0.1:8000/verify'
            subject = 'welcome to Ecommerce world'
            message = f'''
                Hi {user.first_name}, thank you for registering in E-Bouncer.
                OTP-{otp_code}
                Click this link to verify {verification_link}
                '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return Response({'firstName': first_name, 'lastName': last_name, 'email': email, 'verificationLink': verification_link}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(generics.GenericAPIView):
    serializer_class = VerifyOtpSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            input_otp_code = serializer.validated_data['otp_code']
            try:
                user = User.objects.get(email=email)
                db_otp_code = user.otp_code
            except Exception as err:
                return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
            if db_otp_code == input_otp_code:
                user.is_verified = True
                user.save()
                return Response({'verification': user.is_verified}, status=status.HTTP_200_OK)
            elif db_otp_code != input_otp_code:
                return Response({'error': 'OTP code is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
            user.save()
            return Response({'verified': user.is_verified, 'db': str(db_otp_code), 'input_otp_code': str(input_otp_code)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except Exception as err:
                return Response({'msg': str(err)})
            otp_code = str(random.randint(100000, 1000000))
            user.otp_code = otp_code
            user.save()
            verification_link = 'http://127.0.0.1:8000/reset_password'
            subject = 'welcome to Ecommerce world'
            message = f'''
                Hi {user.first_name}, Use this OTP to reset your password.
                OTP-{otp_code}
                Click this link to reset password {verification_link}
                '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return Response({'msg': f"OTP code has been sent to your email. Use it for verification through this link {verification_link}"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp_code']
            try:
                user = User.objects.get(email=email)
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
            if user.otp_code == otp_code:
                user.set_password(password)
                user.save()
                return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            try:
                user = User.objects.get(email=email)
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
            if user.check_password(old_password):
                if old_password != new_password:
                    user.set_password(new_password)
                    return Response({'msg': 'Password changed successfully'})
                return Response({'msg': 'Passwords cannot be the same'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)
