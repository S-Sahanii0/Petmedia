from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Account

@receiver(post_save, sender = Account)
def create_profile(sender, instance, created, **kwargs):
    print("running")
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save, sender = Account)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
