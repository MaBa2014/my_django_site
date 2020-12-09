from django import forms
from .models import Lesson, Teacher, Time_lesson

class PostForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_name', 'teacher', 'time')


class Author_form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name')

class Genre_form(forms.ModelForm):
    class Meta:
        model = Time_lesson
        fields = ('time',)
