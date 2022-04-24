# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
# django.setup()

from Apply.models import Jobs
from Apply.constant_variables import jobs, groups, users
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def remove_all_jobs():
    jobs_to_delete = Jobs.objects.all()
    jobs_to_delete.delete()


def remove_all_users():
    #     getting all the users then loop over that list
    #  so we can just delete all of them except the superuser.
    users_to_delete = User.objects.all()
    for del_user in users_to_delete:
        if del_user.is_superuser:
            continue
        else:
            del_user.delete()


def remove_all_groups():
    groups_to_delete = Group.objects.all()
    groups_to_delete.delete()


def create_jobs():
    remove_all_jobs()
    for job in jobs:
        company = job["company"]
        position = job["position"]
        salary = job["salary"]
        interests = job["interests"]
        new_job = Jobs(company=company, position=position, expected_salary=salary, interests=interests)
        new_job.save()


def create_groups():
    remove_all_groups()
    for group in groups:
        name = group["name"]
        new_group = Group(name=name)
        new_group.save()


def create_users():
    remove_all_users()
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


def run():
    create_jobs()
    create_users()
    create_groups()