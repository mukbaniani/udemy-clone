from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_teacher and request.user == obj.user
