import datetime
from django.shortcuts import render
from .models import Course, Term, Video
from .helpers import get_yt_video_statistics

# Maximum of 1 YouTube API call per video, which resets every hours specified RATE_LIMIT
RATE_LIMIT = 48

# Create your views here.
def index(request):
    sorted_terms = sorted(
        Term.objects.all(),
        key=lambda term: (-term.year, ord(term.semester[0]), -ord(term.semester[1])),
    )

    history = {}
    for term in sorted_terms:
        history[term] = Course.objects.filter(term=term)

    return render(
        request,
        "homepage/index.html",
        {
            "history": history,
        },
    )


def videos(request):
    videos = Video.objects.all()
    for video in videos:

        # Update views if RATE_LIMIT hours have passed, otherwise use cached views
        if (
            datetime.datetime.now(datetime.timezone.utc)
            - datetime.timedelta(hours=RATE_LIMIT)
            >= video.last_updated
        ):
            video.views = int(get_yt_video_statistics(video.source)["viewCount"])
            video.save()

    return render(
        request,
        "homepage/videos.html",
        {
            "videos": sorted(
                videos, key=lambda video: video.views, reverse=True
            )
        },
    )
