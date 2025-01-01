from django.urls import path
from rest_framework import routers

from lesson.views import LessonViewSet

app_name = 'lessons'
router = routers.SimpleRouter()
router.register(r"", LessonViewSet, basename='lesson')
urlpatterns = router.urls

# urlpatterns = [
#   path('lessons/', LessonView.as_view(), name='lesson-list'),
#   path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
# ]