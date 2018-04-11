from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers


class Permissions:
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class CourseViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ['title','description']
    filter_fields = ('id', 'title', 'description', 'teachers', 'price')


class LessonViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class TeacherViewSet(Permissions, viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
