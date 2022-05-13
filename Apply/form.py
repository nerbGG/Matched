from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from Apply.models import Profile, Story
from .constant_variables import fields, education_choices


class loginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.PasswordInput


class FileUploadForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)
    # birthday = forms.DateField(required=False)
    # sport = forms.CharField(max_length=100, required=100)
    resume = forms.FileField(required=False)
    interests_choices = fields
    # edu_choices = forms.ChoiceField(choices=education_choices, required=True)

    # interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=interests_choices)

    class Meta:
        model = Profile
        fields = ('profile_pic', 'resume',)

        # fields = ('profile_pic', 'sport', 'resume', 'edu_choices',)


class SuccessStoryForm(forms.ModelForm):
    success_story = forms.TextInput()

    class Meta:
        model = Story
        fields = ('text',)


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
