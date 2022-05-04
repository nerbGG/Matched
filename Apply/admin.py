from django.contrib import admin
from .models import Profile, Jobs, Education

# , user_Interests

# Register your models here.
admin.site.register(Profile)
# admin.site.register(user_Interests)
admin.site.register(Jobs)
admin.site.register(Education)
