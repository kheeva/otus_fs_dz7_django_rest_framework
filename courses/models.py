from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    teachers = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='courses')
    price = models.IntegerField(null=True, blank=True)
    img_url = models.ImageField(
        verbose_name='Фото',
        max_length=150,
        null=True,
        blank=True,
        #upload_to='static/courses/img/'
    )

    def __str__(self):
        return self.title


class CourseModule(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, related_name='modules')
    number_of_module = models.IntegerField(null=False, blank=False)

    class Meta:
        unique_together = (('course', 'number_of_module'),)

    def __str__(self):
        return '{} {}'.format(self.number_of_module, self.course)


class Lesson(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    module_of_course = models.ForeignKey(CourseModule, models.CASCADE)
    homework = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.module_of_course, self.title)


class Teacher(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}'.format(self.name)
