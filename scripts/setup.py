# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
# django.setup()

from Apply.models import Jobs, Education, Profile
from Apply.constant_variables import jobs, groups, users, education
from django.contrib.auth.models import User, Group


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
        description = job["descriptions"]
        new_job = Jobs(company=company, position=position, expected_salary=salary, interests=interests,
                       description=description)
        new_job.save()


def create_education():
    edu_to_delete = Education.objects.all()
    edu_to_delete.delete()
    for edu in education:
        title= edu["title"]
        school = edu['school']
        tution= edu['tution']
        interest = edu['interests']

        new_education=  Education(title = title, school= school, expected_tution=tution, interests= interest)
        new_education.save()


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
        position = user["position"]
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        new_user.set_password(password)
        new_user.save()
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aenean euismod elementum nisi quis eleifend. Sed ullamcorper morbi tincidunt ornare massa eget egestas. Maecenas accumsan lacus vel facilisis volutpat est velit. Turpis egestas maecenas pharetra convallis. Duis tristique sollicitudin nibh sit amet. Sit amet mauris commodo quis. In iaculis nunc sed augue lacus viverra vitae congue. Sit amet cursus sit amet dictum sit amet justo donec. Mauris pharetra et ultrices neque ornare aenean euismod elementum nisi. Tristique et egestas quis ipsum suspendisse ultrices gravida dictum fusce. Ornare aenean euismod elementum nisi quis eleifend. Diam in arcu cursus euismod quis viverra. Nibh tellus molestie nunc non blandit massa enim nec. Nulla at volutpat diam ut. Quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Volutpat maecenas volutpat blandit aliquam. Id aliquet lectus proin nibh nisl condimentum. Neque ornare aenean euismod elementum. Aliquet lectus proin nibh nisl condimentum id. Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies. Praesent tristique magna sit amet purus. Mi ipsum faucibus vitae aliquet nec ullamcorper sit.Eget nulla facilisi etiam dignissim. Dolor magna eget est lorem ipsum dolor sit. Dignissim suspendisse in est ante in nibh mauris cursus. Lectus magna fringilla urna porttitor. Nam libero justo laoreet sit amet cursus. Id cursus metus aliquam eleifend mi in nulla posuere. Turpis massa sed elementum tempus egestas sed sed risus pretium. Pellentesque sit amet porttitor eget dolor morbi. Ornare massa eget egestas purus. Sit amet consectetur adipiscing elit pellentesque habitant morbi tristique. Tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Pretium quam vulputate dignissim suspendisse in. Sed lectus vestibulum mattis ullamcorper velit sed.Sed nisi lacus sed viverra tellus. In nisl nisi scelerisque eu ultrices vitae auctor eu augue. Lectus arcu bibendum at varius. Lacus sed turpis tincidunt id aliquet risus feugiat. Viverra suspendisse potenti nullam ac tortor vitae purus faucibus. Purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Nunc non blandit massa enim. Venenatis cras sed felis eget velit aliquet. Quam vulputate dignissim suspendisse in. Laoreet suspendisse interdum consectetur libero id.Duis tristique sollicitudin nibh sit. Sit amet nisl purus in mollis nunc sed id. Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor. Accumsan sit amet nulla facilisi morbi tempus iaculis urna id. In nibh mauris cursus mattis molestie a. Montes nascetur ridiculus mus mauris vitae ultricies. Aliquet nibh praesent tristique magna sit amet purus. Egestas sed sed risus pretium quam vulputate. Mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et netus. Donec enim diam vulputate ut. Vel pharetra vel turpis nunc. A diam sollicitudin tempor id eu nisl nunc. Elit sed vulputate mi sit amet mauris. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Lectus urna duis convallis convallis tellus id. Quis imperdiet massa tincidunt nunc pulvinar sapien. Nisi est sit amet facilisis magna etiam tempor orci."
        profile = Profile(user=new_user, success_story=text)
        profile.save()
        group_name = position
        group = Group.objects.get(name=group_name)
        new_user.groups.add(group)
        new_user.is_active = True

def run():
    create_jobs()
    create_users()
    create_groups()
    create_education()
