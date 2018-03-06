from rest_framework import viewsets, permissions

from . import models
from . import serializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
