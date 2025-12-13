from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse("Welcome to <br /> mysite")

def course(request):
    return HttpResponse("Welcome to mysite")

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")