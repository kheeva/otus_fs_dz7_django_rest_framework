from rest_framework import viewsets, permissions

from . import models
from . import serializers


class Permissions:
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class CourseViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class TeacherViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
