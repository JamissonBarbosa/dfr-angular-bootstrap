from django.db import models

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  status = models.BooleanField(default=True)
  lessons = models.ManyToManyField('lesson.Lesson', related_name='courses')

  def __str__(self):
    return self.name

  def __repr__(self):
    return f"<Course: {self.name}>"