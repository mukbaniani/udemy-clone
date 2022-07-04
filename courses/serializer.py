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


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Section


    def create(self, validated_data):
        course = validated_data.get('course')
        count_section = models.Section.objects.filter(course=course).count() + 1
        section = models.Section.objects.create(
            name=f'Section {count_section}: {validated_data.get("name")}',
            course=course
        )
        section.save()
        return section


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Language
