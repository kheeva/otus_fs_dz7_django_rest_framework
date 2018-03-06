from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return self.title


class CourseModule(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    number_of_module = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.number_of_module)


class Lesson(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    module_of_course = models.ForeignKey(CourseModule, models.CASCADE)
    homework = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.description)