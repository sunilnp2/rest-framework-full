from django.db import models
faculty = (('management', 'management'),('science', 'science'),('humanities', 'humanities'))
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    faculty = models.CharField(choices=faculty, max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='item')

    def __str__(self):
        return self.name
