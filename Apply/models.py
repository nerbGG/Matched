from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
from multiselectfield import MultiSelectField

# Create your models here.
# class user_Interests(models.Model):
#     tech = models.BooleanField(default=False)
#     bio = models.BooleanField(default=False)
#     art = models.BooleanField(default=False)
#     athletics = models.BooleanField(default=False)
#     finance = models.BooleanField(default=False)
#     business = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = "user interests"
#
#     def __str__(self):
#         return "user Interests"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    edu_choices = [('hs', 'Highschool'), ('ud', 'Undergraduate'), ('gd', 'Graduate')]
    education = models.CharField(max_length=2, choices=edu_choices, blank=True, default='ud')
    interest_choices = (('tech','Technology'),('med','Medical'),('art','Art'),('ath','Athletics'),
                        ('fin','Finance'),('bus','Business'),)
    interests = MultiSelectField(choices=interest_choices,max_length=5, blank=True)
    # interest = models.OneToOneField(user_Interests, on_delete=models.CASCADE, null=True, blank=True)
    # interests = models.CharField(max_length=100, blank=True)
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

    def __str__(self):
        return "%s 's profile" % self.user.username
