from django.urls import path

from lesson.views import LessonView

app_name = 'lessons'
urlpatterns = [
  path('', LessonView.as_view(), name='lesson-list')
]