from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'Notes'
        managed = True
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    
    def __str__(self) -> str:
        return self.title
