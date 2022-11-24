from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    owner = models.ForeignKey("auth.User", related_name="students", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'Student'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return self.name
