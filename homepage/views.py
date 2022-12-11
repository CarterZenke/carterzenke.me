from django.shortcuts import render
from .models import Course, Term

# Create your views here.
def index(request):
    terms = Term.objects.all().order_by('-year', 'semester')

    history = {}
    for term in terms:
        term.semester = term.get_semester_display()
        history[term] = Course.objects.filter(term=term)

    return render(request, "homepage/index.html", {
        "history" : history,
    })