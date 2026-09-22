from .models import Student
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Student.objects.create(user=instance,
        first_name=instance.first_name,
        last_name=instance.last_name,
        email = instance.email,
        )