from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label=_('პაროლი'), write_only=True, style={'input_type': 'password'})
    password1 = serializers.CharField(label=_('გაიმეორეთ პაროლი'), write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)

    class Meta:
        fields = ['first_name', 'last_name', 'email', 'image', 'password', 'password1', 'token']
        model = User

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password = attrs.get('password')
        if password and password1:
            if password != password1:
                raise serializers.ValidationError(_('პაროლი ერთმანეთს არ ემთხვევა'))
        else:
            raise serializers.ValidationError(_('პაროლის შეყვანა აუცილებელია'))
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            image=validated_data.get('image')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class AuthUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    email = serializers.CharField(label=_('მეილი'), write_only=True)
    password = serializers.CharField(label=_('პაროლი'), write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ['email', 'password', 'token']
        model = User

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                raise serializers.ValidationError(_('მომხმარებელი ვერ მოიძებნა'))
        else:
            raise serializers.ValidationError(_('მეილის და პაროლის შეყვანა სავალდებულოა'))
        attrs['user'] = user
        return attrs
