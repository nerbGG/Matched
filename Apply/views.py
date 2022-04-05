import datetime
import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from Matched.settings import EMAIL_HOST_USER
from Apply.models import Profile
from Apply.constants import ActionNames
from Apply.form import RegistrationForm, AuthenticationForm, loginForm
# from Apply.models import Courses
from Apply.utils import token_generator

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)


def activate_user(user):
    user.is_active = True
    user.save()


def deactivate_user(user):
    user.is_active = False
    user.save()


def register_view(request):
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


login_name = ""


def login_view(request):
    if request.method == "POST":
        form = loginForm
        username = request.POST['username']
        password = request.POST["password"]
        not_active = "Please confirm your account. "
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
    return render(request, "../Templates/home.html", {"activated": True})


def user_profile(request, username):
    if request.method == "POST":
        img = request.POST['img']
        birth_date = request.POST['birthday']
        edu_choices = request.POST['fav_language']
        sport = request.POST['username']
        resume = request.POST['resume']

        user = User.objects.get(username=request.user.username)
        # profile = Profile.objects.get(user=user)
        profile = Profile(user = user,
                          profile_pic=img,
                          birth_date=birth_date,
                          education=edu_choices,
                          sport=sport,
                          resume=resume)

        # profile.profile_pic = img
        # profile.birth_date = birth_date
        # profile.education = edu_choices
        # profile.sport = sport
        # profile.resume = resume
        profile.save()

        return redirect('/')
    else:
        return render(request, "../Templates/birth_education.html")
