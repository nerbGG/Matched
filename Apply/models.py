from django.db import models
from django.contrib.auth.models import User
from .constant_variables import fields, cities
from .validators import validate_file_extension
from multiselectfield import MultiSelectField


class Jobs(models.Model):
    # user = models.ManyToManyField(User, blank=True)
    company = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100000, blank=True)
    expected_salary = models.IntegerField(blank=False)
    company_logo = models.ImageField(blank=True)
    # resume = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', validators=[validate_file_extension])
    # location =
    interest_choices = fields
    interests = MultiSelectField(choices=interest_choices, blank=True)
    locations = MultiSelectField(choices=cities, blank=True)

    def __str__(self):
        return "%s job" % self.position


class Education(models.Model):
    title = models.CharField(max_length=100, blank=False)
    school = models.CharField(max_length=200, blank=False)
    expected_tuition = models.IntegerField(blank=False)
    interest_choices = fields
    interests = MultiSelectField(choices=interest_choices, blank=True)
    locations = MultiSelectField(choices=cities, blank=True)

    def __str__(self):
        return "% s" % self.title


class Story(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, max_length=8000)
    likes = models.IntegerField(blank=True)


# comments for each story
class Comment(models.Model):
    linked_story = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    likes = models.IntegerField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # birth_date = models.DateField(blank=True, null=True)
    edu_choices = [('hs', 'Highschool'), ('ud', 'Undergraduate'), ('gd', 'Graduate')]
    education = models.CharField(max_length=2, choices=edu_choices, blank=True, default='ud')
    interest_choices = fields
    interests = MultiSelectField(choices=interest_choices, blank=True)
    sport = models.CharField(max_length=100, blank=True)
    # pdf only
    resume = models.FileField(upload_to="pdfs/", blank=True)
    profile_pic = models.FileField(upload_to="images/", blank=True)
    # success_story = models.TextField(blank=True, max_length=8000)
    saved_jobs = models.ManyToManyField(Jobs, blank=True)
    locations = MultiSelectField(choices=cities, blank=True)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profile"

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return "%s 's profile" % self.user.username


class UploadModel(models.Model):
    title = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"
