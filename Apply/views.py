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
from Apply.models import Profile, Jobs, Education
from Apply.constants import ActionNames
from Apply.form import RegistrationForm, loginForm, FileUploadForm
# SuccessStoryForm
from Apply.utils import token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import Group
from .constant_variables import fields, education_choices, salary_options, cities
from json import dumps

logger = logging.getLogger(__name__)


def activate_user(user):
    user.is_active = True
    user.save()


def deactivate_user(user):
    user.is_active = False
    user.save()


def home(request):
    # getting the recommended jobs
    if request.user.is_authenticated:
        matched_jobs = []
        matched_education = []
        for job in Jobs.objects.all():
            matches = contains(job.interests, request.user.profile.interests)
            if matches is True:
                matched_jobs.append(job)
        for edu in Education.objects.all():
            matches = contains(edu.interests, request.user.profile.interests)
            if matches is True:
                matched_education.append(edu)
        return render(request, "home.html", {"jobs": matched_jobs,
                                            "education": matched_education})
    else:
        return render(request, "home.html", {"message": "Please Login"})


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
                return render(request, "../templates/home.html",
                              {"activated": False, "message": "Please Check your email for the verification", })

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
            not_active = "Please check you email to activate your account."
            try:
                user = User.objects.get(username=username)
            except:
                user = None
            if user is not None:
                if not user.is_active:
                    return render(request, "registration/login.html",
                                  {"form": form, "message": not_active})
            user = authenticate(request, username=username, password=password)
            user_login = "Please enter a correct username and password. Note that both fields may be case-sensitive."
            if user is not None:
                login(request, user)
                return redirect("/")
                # message = "Welcome back, "+user.first_name+"!"
                # return render(request, "home.html", {"message":message})
            else:
                return render(request, "registration/login.html", {"form": form, "message": user_login})
        else:
            form = loginForm
            return render(request, "registration/login.html", {"form": form})
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
    return render(request, "../Templates/home.html",
                  {"message": "Thank you for activating your account, please login!"})
    # redirect_link = "/profile/" + user.username + "/"
    # return redirect(redirect_link)


def profile_view(request, username):
    if request.user.is_authenticated:
        # this should allow users to search for other users
        user = User.objects.get(username=username)
        # user = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            try:
                profile_pic = request.FILES['profile_pic']
            except:
                if user.profile.profile_pic:
                    profile_pic = user.profile.profile_pic
                else:
                    profile_pic = None
            try:
                resume = request.FILES['resume']
            except:
                if user.profile.resume:
                    resume = user.profile.resume
                else:
                    resume = None

            education = request.POST['education']
            sport = request.POST['sport']
            user = User.objects.get(username=request.user.username)
            tags = request.POST.getlist("tags")
            locations = request.POST.getlist("cities")
            profile = Profile.objects.update_or_create(
                user=user,
                defaults={
                    "profile_pic": profile_pic,
                    # "birth_date": birth_date,
                    "education": education,
                    "sport": sport,
                    "resume": resume,
                    "interests": tags,
                    "locations": locations,
                }, )
            url = "/profile/" + user.username
            return redirect(url)
        form = FileUploadForm()
        fields_json = dumps(fields)
        user_interests_json = dumps(user.profile.interests)
        all_cities_json = dumps(cities)
        user_cities_json = dumps(user.profile.locations)
        return render(request, "profile.html", {
            "profile_user": user,
            "user_interests": user_interests_json,
            "fields": fields_json,
            "all_cities": all_cities_json,
            "user_locations": user_cities_json,
            "education_choices": education_choices,
            "form": form,
        })
    else:
        message = "You need to be logged in to access the profile page"
        return render(request, "home.html", {"message": message})


def test(request):
    user = User.objects.get(username=request.user.username)
    resume = user.profile.resume
    return render(request, 'aws-test.html', {'resume': resume})


# def story_view(request, username):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             story = request.POST['success_story']
#             user = User.objects.get(username=request.user.username)
#             profile = Profile(user=user, success_story=story)
#             profile.save(update_fields=["success_story"])
#             return redirect('/')
#         else:
#             # form = SuccessStoryForm(initial={"success_story": request.user.profile.success_story})
#         return render(request, 'story.html', {"form": form})
#     else:
#         message = "You need to be logged in to access the jobs page"
#         return render(request, "home.html", {"message": message})


# jobs view helpers
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


def get_saved_jobs(request):
    saved_jobs = request.user.profile.saved_jobs.all()
    saved_jobs_dict = {}
    for job in saved_jobs:
        saved_jobs_dict[job.pk] = job
    return saved_jobs_dict


def save_or_remove_job(request):
    job = Jobs.objects.get(id=request.POST["selected_job"])
    saved_jobs = get_saved_jobs(request)
    if job.id in saved_jobs:
        request.user.profile.saved_jobs.remove(job)
    else:
        request.user.profile.saved_jobs.add(job)


def all_jobs_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            save_or_remove_job(request)
            return redirect("/jobs/")
        jobs = Jobs.objects.all()
        saved_jobs_dict = get_saved_jobs(request)

        return render(request, "content.html", {"fields": fields,
                                                "cities": cities,
                                                "contents": jobs,
                                                "saved_jobs": saved_jobs_dict,
                                                "link_url": "/jobs/",
                                                "active": "all",
                                                "salary_options": salary_options, })
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


# pass a filter parameter
def filtered_jobs(request, selected_filter):
    if request.user.is_authenticated:
        if request.method == "POST":
            save_or_remove_job(request)
            url = "/jobs/" + selected_filter
            return redirect(url)
        user = User.objects.get(username=request.user.username)
        user_intrest = user.profile.interests
        matched_jobs = []
        saved_jobs_dict = get_saved_jobs(request)
        for job in Jobs.objects.all():
            if selected_filter == "recommended":
                matches = contains(job.interests, user_intrest)
            elif selected_filter == "saved":
                return render(request, "content.html", {"fields": fields,
                                                        "contents": user.profile.saved_jobs.all(),
                                                        "saved_jobs": saved_jobs_dict,
                                                        "link_url": "/jobs/",
                                                        "active": selected_filter,
                                                        "salary_options": salary_options, })
            else:
                matches = contains_string(job.interests, selected_filter)
            if matches is True:
                matched_jobs.append(job)
        return render(request, "content.html", {"fields": fields,
                                                "contents": matched_jobs,
                                                "saved_jobs": saved_jobs_dict,
                                                "link_url": "/jobs/",
                                                "active": selected_filter,
                                                "salary_options": salary_options, })
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


def filter_by_salary(request, job_list, salary_filter):
    salary_filtered_list = []
    for job in job_list:
        sal = int(salary_filter)
        if job.expected_salary >= sal:
            salary_filtered_list.append(job)
    return salary_filtered_list


def filtered_jobs_salary(request, selected_filter, salary_filter):
    if request.user.is_authenticated:
        if request.method == "POST":
            save_or_remove_job(request)
            url = "/jobs/" + selected_filter + "/" + salary_filter
            return redirect(url)
        user = User.objects.get(username=request.user.username)
        user_intrest = user.profile.interests
        matched_jobs = []
        saved_jobs_dict = get_saved_jobs(request)
        if selected_filter == "saved":
            salary_filtered = filter_by_salary(request, user.profile.saved_jobs.all(), salary_filter)
            return render(request, "content.html", {
                "fields": fields,
                "contents": salary_filtered,
                "saved_jobs": saved_jobs_dict,
                "link_url": "/jobs/",
                "active": selected_filter,
                "salary_filter": int(salary_filter),
                "salary_options": salary_options,
            })
        elif selected_filter == "all":
            salary_filtered = filter_by_salary(request, Jobs.objects.all(), salary_filter)
            return render(request, "content.html", {
                "fields": fields,
                "contents": salary_filtered,
                "saved_jobs": saved_jobs_dict,
                "link_url": "/jobs/",
                "active": selected_filter,
                "salary_filter": int(salary_filter),
                "salary_options": salary_options,
            })
        else:
            for job in Jobs.objects.all():
                if selected_filter == "recommended":
                    matches = contains(job.interests, user_intrest)
                else:
                    matches = contains_string(job.interests, selected_filter)
                if matches is True:
                    matched_jobs.append(job)
            salary_filtered = filter_by_salary(request, matched_jobs, salary_filter)
            return render(request, "content.html", {"fields": fields,
                                                    "contents": salary_filtered,
                                                    "saved_jobs": saved_jobs_dict,
                                                    "link_url": "/jobs/",
                                                    "active": selected_filter,
                                                    "salary_filter": int(salary_filter),
                                                    "salary_options": salary_options,
                                                    })
    else:
        message = "You need to be logged in to access the jobs page"
        return render(request, "home.html", {"message": message})


def job_view(request, previous_page, job_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            save_or_remove_job(request)
        job = Jobs.objects.get(id=job_id)
        saved_jobs = get_saved_jobs(request)
        if previous_page == "all":
            return render(request, "job.html", {"job": job, "saved_jobs": saved_jobs, })
        return render(request, "job.html", {"job": job, "previous_page": previous_page, "saved_jobs": saved_jobs, })
    else:
        return render(request, "home.html", {"message": "You need to be logged in to access the Job page"})

#
# def get_stories(request):
#     story_list = []
#     profile_list = Profile.objects.all()
#     for profile in profile_list:
#         if not profile.success_story == "":
#             story = {"user": profile.user,
#                      "story": profile.success_story,
#                      "interests": profile.interests}
#             story_list.append(story)
#     return story_list


# def all_success_stories(request):
#     if request.user.is_authenticated:
#         # l = list(Profile.objects.all().values_list('success_story', flat=True))
#         story_list = get_stories(request)
#         return render(request, "content.html", {"fields": fields, "contents": story_list,
#                                                 "link_url": "/success-stories/",
#                                                 "active": "all", })
#     else:
#         message = "You need to be logged in to access the stories page"
#         return render(request, "home.html", {"message": message})


# def filtered_success_stories(request, selected_filter):
#     if request.user.is_authenticated:
#         story_list = get_stories(request)
#         user_intrest = Profile.objects.get(user=request.user).interests
#         stories = []
#         for story in story_list:
#             if selected_filter == "recommended":
#                 matches = contains(story["interests"], user_intrest)
#             else:
#                 matches = contains_string(story["interests"], selected_filter)
#             if matches is True:
#                 stories.append(story)
#         return render(request, "content.html", {"fields": fields, "contents": stories,
#                                                 "link_url": "/success-stories/",
#                                                 "active": selected_filter}, )
#     else:
#         message = "You need to be logged in to access the stories"
#         return render(request, "home.html", {"message": message})


def get_education():
    edu_list = []
    for edu in Education.objects.all():
        edu_list.append(edu)
    return edu_list


def all_education(request):
    if request.user.is_authenticated:
        # l = list(Profile.objects.all().values_list('success_story', flat=True))
        edu_list = get_education()
        return render(request, "content.html", {"fields": fields, "contents": edu_list,
                                                "link_url": "/education/",
                                                "active": "all", })
    else:
        message = "You need to be logged in to access the education"
        return render(request, "home.html", {"message": message})


def filtered_education(request, selected_filter):
    if request.user.is_authenticated:
        edu_list = get_education()
        user_intrest = Profile.objects.get(user=request.user).interests
        edu_filter_list = []
        for edu in edu_list:
            if selected_filter == "recommended":
                matches = contains(edu.interests, user_intrest)
            else:
                matches = contains_string(edu.interests, selected_filter)
            if matches is True:
                edu_filter_list.append(edu)
        return render(request, "content.html", {"fields": fields, "contents": edu_filter_list,
                                                "link_url": "/education/",
                                                "active": selected_filter})
    else:
        message = "You need to be logged in to access the stories"
        return render(request, "home.html", {"message": message})


def resources(request):
    if request.user.is_authenticated:
        return render(request, "resources.html", {"link_url":"/resources/"})
    else:
        message = "You need to be logged in to access the stories"
        return render(request, "home.html", {"message": message})
