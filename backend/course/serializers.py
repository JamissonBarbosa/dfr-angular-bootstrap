from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "category", "status", "lessons")
        # extra_kwargs = {
        #   '_id': {'source': 'id'},
        # }
        depth = 1
        #fields = '__all__'