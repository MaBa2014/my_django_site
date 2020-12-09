from django.db import models
from django.db.models import ForeignKey


class Time_lesson(models.Model):
    time = models.CharField(max_length=200, help_text="Введите время начала пары")
    def __str__(self):
        return self.time

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name,)

class Lesson(models.Model):
    lesson_name = models.CharField(null=True, max_length=200, help_text="Введите название предмета")
    teacher = ForeignKey(Teacher,on_delete=models.SET_NULL, null=True)
    time = ForeignKey(Time_lesson, help_text="Выберите время проведения занятия", on_delete = models.CASCADE)
    def __str__(self):
        return self.lesson_name
