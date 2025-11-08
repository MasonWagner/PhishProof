from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Description of the class")

    def __str__(self):
        return f"{self.name} ({self.description})"