# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
# django.setup()

from Apply.models import Jobs
from Apply.constant_variables import jobs, users
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def run():
    job_delete = Jobs.objects.all()
    job_delete.delete()
    for job in jobs:
        company = job["company"]
        position = job["position"]
        salary = job["salary"]
        interests = job["interests"]
        new_job = Jobs(company=company, position=position, expected_salary=salary, interests=interests)
        new_job.save()
    #     getting all the users then loop over that list
    #  so we can just delete all of them except the super user.
    user_delete = User.objects.all()
    for del_user in user_delete:
        if del_user.is_superuser:
            continue
        else:
            del_user.delete()
    #  Creating the new users
    for user in users:
        first_name = user["first_name"]
        last_name = user["last_name"]
        username = user["username"]
        email = user["email"]
        password = user["password1"]
        password2 = user["password2"]
        position = user["position"]
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        new_user.set_password('password1')
        new_user.save()
        group_name = position
        group = Group.objects.get(name=group_name)
        new_user.groups.add(group)
        new_user.is_active = True




