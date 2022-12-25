from django.shortcuts import render
from .models import Course, Term, Video
from .helpers import get_yt_video_statistics

# Create your views here.
def index(request):
    terms = Term.objects.all().order_by("-year", "semester")

    history = {}
    for term in terms:
        history[term] = Course.objects.filter(term=term)

    return render(
        request,
        "homepage/index.html",
        {
            "history": history,
        },
    )

def videos(request):
    return render(request, "homepage/videos.html", {"videos": Video.objects.all()})