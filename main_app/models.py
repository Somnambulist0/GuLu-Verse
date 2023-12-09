from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.jpg')
    bio = models.TextField(blank=True)
    background_color = models.CharField(max_length=7, default="#FFFFFF")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    classification = models.JSONField(default=dict)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    cast = models.TextField(default='')  
    poster_path = models.CharField(max_length=500, null=True, blank=True) 

    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            'title': self.title,
            'genre': self.genre,
            'classification': self.classification,
            'overview': self.overview,
            'vote_average': self.vote_average,
            'release_date': self.release_date.strftime('%Y-%m-%d') if self.release_date else None,
            'cast': self.cast,
            'poster_path': self.poster_path
        }


