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
    data = {}
    try:
        if request.method == "POST":
        # n1 = int(request.GET["num1"])
        # n2 = int(request.GET["num2"])
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = (n1 + n2)
            data = {
                "n1": n1,
                "n2": n2,
                "output": finalans
            }
    except:
        pass
    return render(request, "form.html", data)

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")