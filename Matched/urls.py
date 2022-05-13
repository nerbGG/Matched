"""Matched URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apply import views as apply_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', apply_views.login_view),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", apply_views.home, name="home"),
    path("profile/<username>/", apply_views.profile_view),
    path("accounts/register/", apply_views.register_view),
    path("activate/<uidb64>/<token>", apply_views.verification_view, name="activate"),
    # path("profile/<username>/<edit>/", apply_views.create_profile, name="FileUploadView"),
    path("jobs/", apply_views.all_jobs_view),
    path("job/<previous_page>/<job_id>/", apply_views.job_view),
    path("resume/", apply_views.test),
    path("education/<selected_filter>/", apply_views.filtered_education),
    path("education/", apply_views.all_education),
    path("story/<username>/", apply_views.story_view),
    path("story/<username>/<message>", apply_views.story_view),
    path("story/<username>/<post>/", apply_views.add_comment),
    path("success-stories/", apply_views.stories_view),
    path("success-stories/<selected_filter>/", apply_views.stories_view),
    path("story/<selected_filter>/", apply_views.stories_view),
    path("personal-story/", apply_views.personal_story),
    path("comment/delete/<username>/", apply_views.remove_comment),
    # path("success-stories/<selected_filter>/", apply_views.filtered_success_stories),
    path("jobs/<selected_filter>/<salary_filter>/", apply_views.filtered_jobs_salary),
    path("jobs/<selected_filter>/", apply_views.filtered_jobs),
    path('accounts/login/reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_content.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('resources/', apply_views.resources),
    # path('reset/password/page/', auth_views.PasswordChangeView(template_name='password_reset_form.html'), name='password_reset_change'),
]
# urlpatterns += staticfiles_urlpatterns()
