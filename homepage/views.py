from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    spring_courses = Course.objects.filter(term="Spring", year=2022)
    winter_courses = Course.objects.filter(term="Winter", year=2022)
    fall_courses = Course.objects.filter(term="Fall", year=2021)
    summer_courses = Course.objects.filter(term="Summer", year=2021)
    return render(request, "homepage/index.html", {
        "spring_courses" : spring_courses,
        "winter_courses" : winter_courses,
        "fall_courses" : fall_courses,
        "summer_courses" : summer_courses
    })