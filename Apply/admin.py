from django.contrib import admin
from .models import Profile, Jobs, Education, Story, Comment

# , user_Interests

# Register your models here.
admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Jobs)
admin.site.register(Education)
