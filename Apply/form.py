from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # alternate_name = forms.CharField(required=False)
    # by default, fields are required
    email = forms.EmailField(required=True)
    POSITION_CHOICES = (
        ("jobSeeker", "Job Seeker"),
        ("employer", "Employer"),
        # ("alumni", "Alumni"),
        # ("faculty", "Faculty"),
        # ("staff", "Staff"),
    )

    # se
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=True)

    # select_if_you_already_have_a_unix_account = forms.BooleanField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "position",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password2 == password1:
            raise forms.ValidationError("Both passwords do not match")
        return password2

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     #umb_domain = "umb.edu"
    #     email_domain = email.split("@")[1]
    #     # also need to check if the email in already in database
    #     # if not email_domain == umb_domain:
    #     #     raise forms.ValidationError("Please use  `umb.edu` email")
    #     return email