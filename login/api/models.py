from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering=['id']
        db_table = 'Students'
        # managed = True
        verbose_name = 'Students'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return self.name
