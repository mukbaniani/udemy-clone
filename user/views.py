from rest_framework import generics, status, permissions
from .models import User
from . import serializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class AuthUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.AuthUserSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data.get('user')
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
