from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Giveaway(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=540)
    image = models.ImageField(upload_to="giveaway_image")
    created = models.DateField(auto_now=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"