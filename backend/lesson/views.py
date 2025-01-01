#from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from lesson.models import Lesson
from lesson.serializer import LessonSerializer


# class LessonViewSet(ModelViewSet):
#   queryset = Lesson.objects.all()
#   serializer_class = LessonSerializer


class LessonViewSet(ViewSet):
  def list(self, request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self, request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    serializer = LessonSerializer(lesson)
    return Response(serializer.data)
  
  def update(self, request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    serializer = LessonSerializer(lesson, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def destroy(self, request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# class LessonView(APIView):
#   def get(self, request):
#     lessons = Lesson.objects.all()
#     serializer = LessonSerializer(lessons, many=True)
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = LessonSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

# class LessonDetailView(APIView):
#   def get(self, request, pk):
#     #lesson = Lesson.objects.get(pk=pk)
#     lesson = get_object_or_404(Lesson, pk=pk)
#     serializer = LessonSerializer(lesson)
#     return Response(serializer.data)
  
#   def put(self, request, pk):
#     lesson = get_object_or_404(Lesson, pk=pk)
#     serializer = LessonSerializer(lesson, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk):
#     lesson = get_object_or_404(Lesson, pk=pk)
#     lesson.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)