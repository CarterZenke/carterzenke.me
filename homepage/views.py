import datetime
from django.shortcuts import render
from .models import Course, Term, Video
from .helpers import get_yt_video_statistics

# Maximum of 1 YouTube API call per video, which resets every hours specified RATE_LIMIT
RATE_LIMIT = 48

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
    for video in Video.objects.all():

        # Update views if RATE_LIMIT hours have passed, otherwise use cached views
        if datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=RATE_LIMIT) >= video.last_updated:
            video.views = get_yt_video_statistics(video.source)["viewCount"]
            video.save()
        
    return render(request, "homepage/videos.html", {"videos": Video.objects.all()})