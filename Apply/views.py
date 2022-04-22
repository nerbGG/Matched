import os
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.views import View
# from Matched.settings import EMAIL_HOST_USER
import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from Apply.models import Profile, Jobs
from Apply.constants import ActionNames
from Apply.form import RegistrationForm, loginForm, ProfileForm, SuccessStoryForm
from Apply.utils import token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import Group
from .constant_variables import fields

logger = logging.getLogger(__name__)


def activate_user(user):
    user.is_active = True
    user.save()


def deactivate_user(user):
    user.is_active = False
    user.save()


def register_view(request):
    if not request.user.is_authenticated:
        # send_activation_email(request)
        """"""
        # send_activation_email(request)
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                # path to view getting the domain we are on relative url to verification encode uid token
                user = User.objects.get(username=request.POST["username"])
                group_name = request.POST["position"]
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                deactivate_user(user)
                send_activation_email(request, user)
                return render(request, "../templates/home.html", {"activated": False})
        else:
            form = RegistrationForm()
        return render(request, "../templates/registration/registration.html", {"form": form})
    else:
        message = "You need to be logged out to access the registration page"
        return render(request, "home.html", {"message": message})


login_name = ""


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm
            username = request.POST['username']
            password = request.POST["password"]
            not_active = "Please confirm your account."
            user = User.objects.get(username=username)
            if user is not None:
                if not user.is_active:
                    return render(request, "../templates/registration/login.html", {"form": form, "message": not_active})
            user = authenticate(request, username=username, password=password)
            user_login = " Please enter a correct username and password. Note that both fields may be case-sensitive."
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, "../templates/registration/login.html", {"form": form, "message": user_login})
        else:
            form = loginForm
            return render(request, "../templates/registration/login.html", {"form": form})
    else:
        message = "You need to be logged out to access the login page"
        return render(request, "home.html", {"message": message})

def send_activation_email(request, user):
    # karthiks code working for email send.
    # email_subject = ActionNames.EmailSubject
    #
    # user_email = request.POST.get("email")
    # send_mail(email_subject, "Hello!!", "team.matched@gmail.com", ["ahsanshuja1127@gmail.com"])
    # logger.debug(f"Verification Email has been sent to {user_email}")
    global login_name
    login_name = user.username
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    link = reverse(
        "activate",
        kwargs={"uidb64": uidb64, "token": token_generator.make_token(user)},
    )
    activity_url = f"http://{domain}{link}"
    email_subject = ActionNames.EmailSubject
    email_body = f"Hi {user.first_name} please use this link to verify the account\n {activity_url}"
    user_email = request.POST.get("email")
    email = EmailMessage(
        email_subject,
        email_body,
        "noreply@TeamMatched.com",
        [user_email],
    )
    email.send()
    logger.debug(f"Verification Email has been sent to {user_email}")


def verification_view(request, uidb64, token):
    user = User.objects.get(username=login_name)
    activate_user(user)
    logger.debug("Verification link has been generated")
    # return render(request, "../Templates/home.html", {"activated": True})
    redirect_link = "/profile/" + user.username + "/"
    return redirect(redirect_link)


# def user_profile(request, username):
#     if request.method == "POST":
#         img_st = request.POST['img']
#         birth_date = request.POST['birthday']
#         edu_choices = request.POST['fav_language']
#         sport = request.POST['username']
#         resume = request.POST['resume']
#

#         with open(img_st, "rb") as img_file:
#             img = base64.b64decode(img_file.read())
#
#         user = User.objects.get(username=request.user.username)
#         # profile = Profile.objects.get(user=user)
#         tags = request.POST.getlist("tags")
#         profile = Profile(user=user,
#                           profile_pic=img,
#                           birth_date=birth_date,
#                           education=edu_choices,
#                           sport=sport,
#                           resume=resume,
#                           interests=tags)
#
#         profile.save()
#
#         return redirect('/')
#     else:
#         return render(request, "profile.html")


def create_profile(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            birth_date = request.POST['birthday']
            profile_pic = request.FILES['profile_pic']
            edu_choices = request.POST['edu_choices']
            sport = request.POST['sport']
            resume = request.FILES['resume']
            # intrests = request.POST['interests']
            # with open(img_st, "rb") as img_file:
            #     img = base64.b64decode(img_file.read())
            user = User.objects.get(username=request.user.username)
            tags = request.POST.getlist("tags")
            profile = Profile(user=user,
                              profile_pic=profile_pic,
                              birth_date=birth_date,
                              education=edu_choices,
                              sport=sport,
                              resume=resume,
                              interests=tags)
            profile.save()
            return redirect("/")
        else:
            form = ProfileForm()
        return render(request, "profile.html", {'form': form, "fields": fields})
    else:
        message = "You need to be logged in to access the profile page"
        return render(request, "home.html", {"message": message})


def test(request):
    user = User.objects.get(username=request.user.username)
    resume = user.profile.resume
    return render(request, 'aws-test.html', {'resume': resume})


def story_view(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            story = request.POST['success_story']
            user = User.objects.get(username=request.user.username)
            profile = Profile(user=user, success_story=story)
            profile.save(update_fields=["success_story"])
            return redirect('/')
        else:
            form = SuccessStoryForm()
        return render(request, 'story.html', {"form": form})
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


def all_jobs_view(request):
    if request.user.is_authenticated:
        jobs = Jobs.objects.all()
        return render(request, "content.html", {"fields": fields, "contents": jobs,
                                                "link_url": "/jobs/",
                                                "active": "all"}, )
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


def contains(list1, list2):
    var = False
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                var = True
    return var


def contains_string(list, string):
    var = False
    for item1 in list:
        if item1 == string:
            var = True
    return var


# pass a filter parameter
def filtered_jobs(request, selected_filter):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user_intrest = user.profile.interests
        matched_jobs = []
        for job in Jobs.objects.all():
            if selected_filter == "recommended":
                matches = contains(job.interests, user_intrest)
            else:
                matches = contains_string(job.interests, selected_filter)
            if matches is True:
                matched_jobs.append(job)
        return render(request, "content.html", {"fields": fields, "contents": matched_jobs,
                                                "link_url": "/jobs/",
                                                "active": selected_filter}, )
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


def all_success_stories(request):
    if request.user.is_authenticated:
        profile_list = Profile.objects.all()
        story_list = []
        for profile in profile_list:
            story = {"user": profile.user.username,
                     "story": profile.success_story,
                     "interests": profile.interests}
            story_list.append(story)
        return render(request, "content.html", {"fields": fields, "contents": story_list,
                                                "link_url": "/success-stories/",
                                                "active": "all", })
    else:
        message = "You need to be logged in to access the stories page"
        return render(request, "home.html", {"message": message})


def filtered_success_stories(request, selected_filter):
    if request.user.is_authenticated:
        profile_list = Profile.objects.all()
        user = User.objects.get(username=request.user.username)
        user_intrest = user.profile.interests
        story_list = []
        for profile in profile_list:
            story = {"user": profile.user.username,
                     "story": profile.success_story,
                     "interests": profile.interests}
            story_list.append(story)
        stories = []
        for story in story_list:
            if selected_filter == "recommended":
                matches = contains(story["interests"], user_intrest)
            else:
                matches = contains_string(story["interests"], selected_filter)
            if matches is True:
                stories.append(story)
        return render(request, "content.html", {"fields": fields, "contents": stories,
                                                "link_url": "/success-stories/",
                                                "active": selected_filter}, )
    else:
        message = "You need to be logged in to access the stories"
        return render(request, "home.html", {"message": message})
