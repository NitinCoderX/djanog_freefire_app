from django.db import models

# Create your models here.
class Video(models.Model):
    url = models.TextField(max_length=350,unique=True)


class Contact(models.Model):
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=540)

    def __str__(self):
        return f"{self.email} send a message"
