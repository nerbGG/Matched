from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    # edu_choices = [('hs', 'Highschool'), ('ud', 'Undergraduate'), ('gd', 'Graduate')]
    education = models.CharField(max_length=100)
    interests = models.CharField(max_length=100, blank=True)
    sport = models.CharField(max_length=100)
    # pdf only
    resume = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', validators=[validate_file_extension])
    profile_pic = models.ImageField(blank=True)
    success_story = models.TextField(blank=True)

    # location=
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profile"

    def __unicode__(self):
        return self.user.username
