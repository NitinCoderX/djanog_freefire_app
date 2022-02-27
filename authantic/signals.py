from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from authantic.models import Profile,PhoneUserRelationship

@receiver(post_save,sender=User)
def create_profile(sender,instance,created ,**kwargs):
    if created:
        profile = Profile.objects.create(User_model=instance)
        profile.save()

@receiver(post_delete,sender=PhoneUserRelationship)
def delete_phone(sender,instance,**kwargs):
    phone = instance.phone
    phone.delete()