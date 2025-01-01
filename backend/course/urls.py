from rest_framework import routers

from course.views import CourseViewSet


app_name = 'courses'
router = routers.SimpleRouter()
router.register(r"", CourseViewSet, basename='course')
urlpatterns = router.urls