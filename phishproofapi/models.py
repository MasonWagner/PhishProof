from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Description of the class")
    students = models.ManyToManyField(User, related_name='classes', blank=True)

    def __str__(self):
        return f"{self.name} ({self.description})"
class Challenges(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Description of the challenge")
    students = models.ManyToManyField(User, related_name='challenges', blank=True)

    def __str__(self):
        return f"{self.name} ({self.description})"