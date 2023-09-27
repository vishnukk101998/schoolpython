
from django.db import models


# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
