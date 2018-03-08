from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'title', 'description')


class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseModule
        fields = ('course', 'number_of_module')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('id', 'title', 'description', 'module_of_course', 'homework')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('id', 'name')
