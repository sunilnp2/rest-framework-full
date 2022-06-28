from django.db import models

# Create your models here
class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.FloatField()
    color = models.CharField(max_length=50)
    height = models.CharField(max_length=50)

    def __str__(self):
        return self.name
