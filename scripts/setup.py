# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
# django.setup()

from Apply.models import Jobs, Education, Profile, Story, Comment
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
        locations = job["locations"]
        description = job["descriptions"]
        new_job = Jobs(company=company, position=position, expected_salary=salary, interests=interests,
                       locations=locations,
                       description=description)
        new_job.save()


def create_education():
    edu_to_delete = Education.objects.all()
    edu_to_delete.delete()
    for edu in education:
        title = edu["title"]
        school = edu['school']
        tuition = edu['tuition']
        interest = edu['interests']
        locations = edu["locations"]
        new_education = Education(title=title, school=school, expected_tuition=tuition, locations=locations,
                                  interests=interest)
        new_education.save()


def create_groups():
    remove_all_groups()
    for group in groups:
        name = group["name"]
        new_group = Group(name=name)
        new_group.save()


def create_stories(user, text):
    s = Story(author=user, text=text)
    s.save()


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
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aenean euismod elementum nisi quis eleifend. Sed ullamcorper morbi tincidunt ornare massa eget egestas. Maecenas accumsan lacus vel facilisis volutpat est velit. Turpis egestas maecenas pharetra convallis. Duis tristique sollicitudin nibh sit amet. Sit amet mauris commodo quis. In iaculis nunc sed augue lacus viverra vitae congue. Sit amet cursus sit amet dictum sit amet justo donec. Mauris pharetra et ultrices neque ornare aenean euismod elementum nisi. Tristique et egestas quis ipsum suspendisse ultrices gravida dictum fusce. Ornare aenean euismod elementum nisi quis eleifend. Diam in arcu cursus euismod quis viverra. Nibh tellus molestie nunc non blandit massa enim nec. Nulla at volutpat diam ut. Quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Volutpat maecenas volutpat blandit aliquam. Id aliquet lectus proin nibh nisl condimentum. Neque ornare aenean euismod elementum. Aliquet lectus proin nibh nisl condimentum id. Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies. Praesent tristique magna sit amet purus. Mi ipsum faucibus vitae aliquet nec ullamcorper sit.Eget nulla facilisi etiam dignissim. aliquam eleifend mi in nulla posuere. Turpis massa sed elementum tempus egestas sed sed risus pretium. Pellentesque sit amet porttitor eget dolor morbi. Ornare massa eget egestas purus."
        create_stories(new_user, text)
        profile = Profile(user=new_user)
        profile.save()
        group_name = position
        group = Group.objects.get(name=group_name)
        new_user.groups.add(group)
        new_user.is_active = True


def run():
    create_groups()
    create_jobs()
    create_users()
    create_education()
