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
    interest_choices = (('tech', 'Technology'), ('med', 'Medical'), ('art', 'Art'), ('ath', 'Athletics'),
                        ('fin', 'Finance'), ('bus', 'Business'),)
    interests = MultiSelectField(choices=interest_choices, max_length=5, blank=True)

    sport = models.CharField(max_length=100)
    # pdf only
    resume = models.FileField(upload_to="pdfs/")
    profile_pic = models.FileField(upload_to="images/")
    # profile_pic = models.ImageField(blank=True)
    success_story = models.TextField(blank=True)

    # location=
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profile"

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return "%s 's profile" % self.user.username


class Jobs(models.Model):
    user = models.ManyToManyField(User)
    position = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100000, blank=False)
    expected_salary = models.IntegerField()
    company_logo = models.ImageField(blank=True)
    resume = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', validators=[validate_file_extension])

    def __str__(self):
        return "%s job" % self.user.username


class UploadModel(models.Model):
    title = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"
