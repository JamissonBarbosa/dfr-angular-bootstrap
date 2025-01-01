from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lessons/', include('lesson.urls', namespace='lessons')),
    path('api/courses/', include('course.urls', namespace='courses')),
]
