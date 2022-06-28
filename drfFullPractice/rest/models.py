from django.db import models

# Create your models here.

class Stud(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# models for serializer relations 

class Singer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.title 

