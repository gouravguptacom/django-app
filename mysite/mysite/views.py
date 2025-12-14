from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm
from service.models import Service
from news.models import News

def home_page(request):
    news_data = News.objects.all()
    
    # sd = News.objects.filter(news_title="title") # exact match
    # sd = News.objects.filter(news_title__icontains="t") # like match of sql

    # DONT USE NEGETIVE INDEX IN RANGE EX. [:-1]
    service_data = Service.objects.all().order_by("service_title")[:1] # asc
    # service_data = Service.objects.all().order_by("service_title") # asc
    # service_data = Service.objects.all().order_by("-service_title") # desc
    # print(list(map(lambda x: x.service_icon, service_data)))

    data = {
        "title": "Home Page",
        "news_data": news_data,
        "service_data": [],
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
    if request.method == "GET":
        output = request.GET.get("output")
    return render(request, "services.html", { "output": output })

def marksheet(request):
    if request.method == "POST":
        sub1 = eval(request.POST.get("sub1"))
        sub2 = eval(request.POST.get("sub2"))
        sub3 = eval(request.POST.get("sub3"))
        sub4 = eval(request.POST.get("sub4"))
        sub5 = eval(request.POST.get("sub5"))
        t = sum([sub1, sub2, sub3, sub4, sub5])
        p = t * 100 / 500;
        if p >= 60:
            d = "First Div"
        elif p >= 48:
            d = "Second Div"
        elif p >= 35:
            d = "Third Div"
        else:
            d = "Fail"
        data = {
            "total": t,
            "per": p,
            "div": d
        }
        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")

def evenodd(request):
    c = ""
    if request.method == "POST":
        if request.POST.get("num1") == "":
            return render(request, "evenodd.html", {"error":True})

        n1 = eval(request.POST.get("num1"))
        if n1 % 2 == 0:
            c = "Even"
        else:
            c = "Odd"

    return render(request, "evenodd.html", {"c":c})

def calculator(request):
    c = ""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "x":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = "Invalid Operation"

    return render(request, "calculator.html", {"c":c})

def news_details(request, id):
    news_detail = News.objects.get(id=id)
    data = {
        "news_detail": news_detail
    }
    return render(request, "news-details.html", data)

def submit_form(request):
    finalans = 0
    data = {}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = (n1 + n2)
            data = {
                "n1": n1,
                "n2": n2,
                "output": finalans
            }
            
            return HttpResponse(finalans)
    except:
        pass

def form(request):
    fn = usersForm()
    finalans = 0
    data = {"form":fn}
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
                "form": fn,
                "output": finalans
            }
            
            url = "/services/?output={}".format(finalans)
            return HttpResponseRedirect(url)
            # return redirect(url)
    except:
        pass
    return render(request, "form.html", data)

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")