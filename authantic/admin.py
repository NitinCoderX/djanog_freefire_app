from django.contrib import admin

# Register your models here.
from authantic.models import Profile,Phone,PhoneUserRelationship

# Register your models here.
admin.site.register(Profile)
admin.site.register(PhoneUserRelationship)
admin.site.register(Phone)