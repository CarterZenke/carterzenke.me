from django.shortcuts import render
from .models import Course, Term

# Create your views here.
def index(request):
    terms = Term.objects.all().order_by('-year', 'semester')

    history = {}
    for term in terms:
        history[term] = Course.objects.filter(term=term)
        for course in history[term]:
            course.term.semester = course.term.get_semester_display()

    return render(request, "homepage/index.html", {
        "history" : history,
    })