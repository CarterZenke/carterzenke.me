import datetime
from django.db.models import Q
from django.shortcuts import render
from .models import Course, Term, Video
from .helpers import get_yt_video_statistics

# Maximum of 1 YouTube API call per video, which resets every number of hours specified RATE_LIMIT
RATE_LIMIT = 24 * 7

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

    q = request.GET.get("q", None)
    sort = request.GET.get("sort", None)

    # Filter videos if q provided
    if q:
        videos = Video.objects.filter(
            Q(title__icontains=q) | Q(tags__name__icontains=q)
        )
    else:
        videos = Video.objects.all()

    # Update views if RATE_LIMIT hours have passed, otherwise use cached views
    for video in videos:
        if (
            datetime.datetime.now(datetime.timezone.utc)
            - datetime.timedelta(hours=RATE_LIMIT)
            >= video.last_updated
        ):
            video.views = int(get_yt_video_statistics(video.source)["viewCount"])
            video.save()

    # Define sort function
    if sort == "title-ascending":
        sort_function = lambda video: video.title
        reverse = False
    elif sort == "title-descending":
        sort_function = lambda video: video.title
        reverse = True
    elif sort == "views-ascending":
        sort_function = lambda video: video.views
        reverse = False
    else:
        sort_function = lambda video: video.views
        reverse = True

    return render(
        request,
        "homepage/videos.html",
        {
            "videos": sorted(videos, key=sort_function, reverse=reverse),
            "count": len(videos),
            "q": q,
            "sort": sort,
        },
    )
