from django.db import models

# Create your models here.
# imagine models/schema

# Serializers part 4.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # lives within cat class

    def __str__(self):
        return self.name
    