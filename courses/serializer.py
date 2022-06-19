from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Category


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Course


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Rates
