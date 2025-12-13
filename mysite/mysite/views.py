from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    data = {
        "title": "Home Page",
        "bdata": "Welcome to razorfish",
        "clist": ["PHP", "Java", "Django"],
        "numbers": [10, 20, 30, 40, 50],
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

def services(request):
    return render(request, "services.html")

def form(request):
    finalans = 0
    try:
        # n1 = int(request.GET["num1"])
        # n2 = int(request.GET["num2"])
        n1 = request.GET.get("num1")
        n2 = request.GET.get("num2")
        finalans = (n1 + n2)
    except:
        pass
    return render(request, "form.html", { "output": finalans })

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")