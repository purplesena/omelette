from asyncio.windows_events import NULL
from hashlib import blake2b
from pickle import TRUE
from ssl import create_default_context
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

GENDERS = (
    ('m', 'male'),
    ('f', 'female'),
    ('nb', 'non binary')
)

SEXUALITY = (
    ('w', 'like women'),
    ('m', 'like men'),
    ('bi', 'like both')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default="hey")
    physical_desc = models.CharField(max_length=500, default="georgeous")
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=5)
    gender = models.CharField(choices=GENDERS, max_length=20)
    sexuality = models.CharField(choices=SEXUALITY, max_length=20, default='bi')
    img1 = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    img2 = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    img3 = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    img4 = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    likers = models.ManyToManyField(User, blank=True, related_name='likers')
    liked = models.ManyToManyField(User, blank=True, related_name='liked')

    def find_age(self):
        import datetime
        self.age = (datetime.date.today() - self.birthdate)/365

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()