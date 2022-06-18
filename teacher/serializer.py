from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Teacher

class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['profession', 'linkedin_address', 'bio']
        model = models.Teacher
