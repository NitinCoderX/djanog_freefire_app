from django.db import models
from django.contrib.auth.models import User
from authantic.helper import get_random_slug


# Create your models here.
class Profile(models.Model):
    first_name= models.CharField(max_length=30,blank=True)
    last_name= models.CharField(max_length=30,blank=True)
    User_model = models.OneToOneField(User,on_delete=models.CASCADE)
    birthday = models.DateField(default="2020-12-12")
    bio = models.TextField(max_length=250,blank=True)
    avatar = models.ImageField(upload_to="profilePic/",default = "avatar.jpg")
    slug = models.CharField(max_length=50,unique=True,blank=True)
    created = models.DateField(auto_now=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.User_model.username} {self.last_name}"


    def save(self, *args, **kwargs):
        self.slug = get_random_slug(self.User_model.username)
        super(Profile, self).save(*args, **kwargs)

class Phone(models.Model):
    phone_number= models.CharField(max_length=12)

    def __str__(self):
        return f"{self.phone_number}"

class PhoneUserRelationship(models.Model):
    phone = models.ForeignKey(Phone,on_delete=models.CASCADE)
    User = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.phone} -> {self.User} "