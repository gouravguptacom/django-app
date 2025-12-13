from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    data = {
        "title": "Home Page",
        "bdata": "Welcome to razorfish",
        "clist": ["PHP", "Java", "Django"],
        "student_details": [
            {"name": "gaurav gupta", "phone": 983248723},
            {"name": "testing kumar", "phone": 23612323}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to <br /> mysite")

def course(request):
    return HttpResponse("Welcome to mysite")

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")