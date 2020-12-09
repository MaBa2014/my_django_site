from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.lessons_list, name='lessons_list'),
    re_path(r'^lesson/new/$', views.lesson_new, name='Lesson_new'),
]

