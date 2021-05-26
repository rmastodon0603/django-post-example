from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
