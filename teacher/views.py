from rest_framework import generics, permissions
from . import models, serializer, permission
from rest_framework.response import Response


class CreateTeacherView(generics.CreateAPIView):
    serializer_class = serializer.TeacherSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        teacher_serializer = self.serializer_class(data=request.data)
        teacher_serializer.is_valid(raise_exception=True)
        teacher = teacher_serializer.save()
        if not teacher.user.is_teacher:
            teacher.user.is_teacher = True
            teacher.user.save()
        return Response({'result': 'teacher-added'})


class UpdateTeacherView(generics.UpdateAPIView):
    serializer_class = serializer.TeacherUpdateSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = (permission.IsTeacher,)
