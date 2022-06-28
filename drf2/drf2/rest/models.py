from django.db import models

# Create your models here.

class Information(models.Model):
    name= models.CharField(max_length=200)
    age = models.IntegerField()
    add = models.CharField(max_length=50)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.name

