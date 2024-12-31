from rest_framework import serializers

from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
      model = Lesson
      fields = ("id", "name", "youtube_url")
      # extra_kwargs = {
      #   '_id': {'source': 'id'},
      # }
      
      #fields = '__all__'