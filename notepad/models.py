from django.db import models

# Create your models here.

class Notepad(models.Model):
    name = models.CharField(max_length=50)
    note = models.TextField()
    dt_creation = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name 