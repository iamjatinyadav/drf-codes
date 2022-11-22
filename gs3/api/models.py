from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        db_table = 'Student'
        # managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return self.name 
