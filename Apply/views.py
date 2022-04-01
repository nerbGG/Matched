import datetime
import logging

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

from Apply.constants import ActionNames
from Apply.form import RegistrationForm
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
