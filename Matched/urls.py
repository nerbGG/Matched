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
    # path('profile/<username>/', apply_views.user_profile),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/register/", apply_views.register_view),
    path("activate/<uidb64>/<token>", apply_views.verification_view, name="activate"),
    path("profile/<username>/", apply_views.FileUploadView, name="FileUploadView")
]
# urlpatterns += staticfiles_urlpatterns()
