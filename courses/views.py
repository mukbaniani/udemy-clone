from rest_framework import viewsets, permissions
from . import models, serializer


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializer.CategorySerializer
