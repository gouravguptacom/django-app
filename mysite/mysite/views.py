from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("Welcome to <br /> mysite")

def course(request):
    return HttpResponse("Welcome to mysite")

def course_details(request, courseid: int):
    return HttpResponse(f"entered id: {courseid}")