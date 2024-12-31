from rest_framework.views import APIView
from rest_framework.response import Response

from lesson.models import Lesson
from lesson.serializer import LessonSerializer


class LessonView(APIView):
  def get(self, request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)