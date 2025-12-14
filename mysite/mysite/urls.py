"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from mysite import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("admin/", admin.site.urls, name="secret"),
    path("about/", views.aboutUs, name="about"),
    path("form/", views.form, name="form"),
    path("course/", views.course),
    path("evenodd/", views.evenodd),
    path("services/", views.services),
    path("marksheet/", views.marksheet),
    path("calculator/", views.calculator),
    path("submit-form/", views.submit_form, name="submit-form"),
    path("news_details/<id>", views.news_details),
    path("course/<int:courseid>", views.course_details),
    # path("course/<slug:coursename>", views.course_details),
]
