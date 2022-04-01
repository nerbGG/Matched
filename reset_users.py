from django.contrib.auth.models import User

all_users = User.objects.all()

for user in all_users:
    if not user.username == "nerb":
        User.objects.get(username=user.username).delete()

