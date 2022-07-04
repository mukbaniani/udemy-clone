from rest_framework import viewsets, permissions
from . import models, serializer
from teacher.permission import IsTeacher


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializer.CategorySerializer


class CourseAddView(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    permission_classes = (IsTeacher,)
    serializer_class = serializer.CourseSerializer


class CreateRateView(viewsets.ModelViewSet):
    queryset = models.Rates.objects.all()
    serializer_class = serializer.RateSerializer


class AddSection(viewsets.ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializer.SectionSerializer


class AddLanguage(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializer.LanguageSerializer
    permission_classes = (permissions.IsAdminUser,)
