from django.db import models

# Create your models here.
class Lesson(models.Model):
  name = models.CharField(max_length=50)
  youtube_url = models.CharField(max_length=11)

  def __str__(self):
    return self.name

  def __repr__(self):
    return f"<Lesson: {self.name}>"