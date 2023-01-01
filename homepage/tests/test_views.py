import datetime
from django.test import Client
from django.test import TestCase
from homepage.models import Course, Term, Video, VideoTag
import random

TERMS = [
    {"semester": "Winter", "year": 2022},
    {"semester": "Spring", "year": 2022},
    {"semester": "Summer", "year": 2022},
    {"semester": "Fall", "year": 2022},
    {"semester": "Winter", "year": 2023},
    {"semester": "Spring", "year": 2023},
    {"semester": "Summer", "year": 2023},
    {"semester": "Fall", "year": 2023},
]

COURSES = [
    {
        "title": "Introduction to Computer Science",
        "number": "CS50",
        "school": "Harvard College",
        "role": "Preceptor",
    },
    {
        "title": "Computer Science for Lawyers",
        "number": "HLS 2260",
        "school": "Harvard Law School",
        "role": "Preceptor",
    },
    {
        "title": "Computer Science for Managers",
        "number": "HBS 7475 & 7473",
        "school": "Harvard Business School",
        "role": "Preceptor",
    },
    {
        "title": "Intensive Introduction to Computer Science",
        "number": "CSCI E-50",
        "school": "Harvard Extension School",
        "role": "Teaching Fellow",
    },
    {
        "title": "Introduction to Computer Science",
        "number": "CS50",
        "school": "Harvard College",
        "role": "Preceptor",
    },
]

SORTED_SEASONS = ["Fall", "Summer", "Spring", "Winter"]

VIDEOS = [
    {
        "title": "Week 1 Supersection",
        "source": "MEO1kAawOXQ",
        "slides": "https://docs.google.com/presentation/d/1E5yqTTe7ujw0Q7m4JmFDejKaqa5ayarhgeuyWppyeTk/edit?usp=sharing",
        "code": "",
        "last_updated": datetime.datetime.now(datetime.timezone.utc),
        "views": 1000,
    },
    {
        "title": "Week 2 Section",
        "source": "fJJfbKccYWg",
        "slides": "",
        "code": "",
        "last_updated": datetime.datetime.now(datetime.timezone.utc),
        "views": 138,
    },
    {
        "title": "Week 3 Section",
        "source": "n7Kxdd4iWP8",
        "slides": "https://docs.google.com/presentation/d/1DaajVkxPHAZRO6Fxg7tbIN4_R4dmn2XapnpNbL_x2oM/edit?usp=sharing",
        "code": "https://cs50.harvard.edu/college/2022/fall/sections/3/",
        "last_updated": datetime.datetime.now(datetime.timezone.utc),
        "views": 250,
    },
]

TAGS = [
    {"name": "functions"},
]


class HomepageTestCase(TestCase):
    @classmethod
    def setUpTestData(self):

        # Shuffle terms and add to database
        random.shuffle(TERMS)
        for term in TERMS:
            Term.objects.create(**term)

        # Shuffle courses and add to database
        random.shuffle(COURSES)
        for course in COURSES:
            Course.objects.create(
                **course, term=Term.objects.get(pk=random.randint(1, len(TERMS)))
            )

    def setUp(self):
        self.client = Client()
        self.response = self.client.get("/")

    def test_homepage_status(self):
        """Homepage returns 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Homepage uses index.html and layout.html from homepage app"""
        self.assertTemplateUsed(self.response, "homepage/index.html")
        self.assertTemplateUsed(self.response, "homepage/layout.html")

    def test_teaching_tab_active(self):
        """Teaching tab is labeled as active"""
        self.assertContains(
            self.response,
            '<a class="nav-link active" aria-current="page" href="/">Teaching</a>',
        )

    def test_name_included(self):
        """Name is included in homepage"""
        self.assertContains(self.response, "Carter Zenke")

    def test_all_terms_listed_once(self):
        """All terms appear exactly once in HTML"""
        for term in TERMS:
            self.assertContains(
                self.response, f"{term['semester']} {term['year']}", count=1
            )

    def test_terms_sorted_by_year(self):
        """Terms are sorted by most to least recent year"""
        history = self.response.context["history"]
        terms = list(history.keys())
        for i in range(len(terms) - 1):
            self.assertGreaterEqual(terms[i].year, terms[i + 1].year)

    def test_terms_sorted_by_semester(self):
        """Terms are sorted by season within a given year"""
        history = self.response.context["history"]
        terms = [term for term in list(history.keys()) if term.year == 2022]

        for i, term in enumerate(terms):
            self.assertEquals(term.semester, SORTED_SEASONS[i])

    def test_courses_listed(self):
        """All courses appear in HTML"""
        for course in COURSES:
            self.assertContains(
                self.response,
                f'<h6><span style="font-weight: 700">{course["title"]} ({course["number"]})</span>, {course["school"]}</h6> <p style="color: grey;">{ course["role"] }</p>',
                html=True,
            )


class VideosTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        """Add test videos to database"""

        # Add tags to database
        for tag in TAGS:
            VideoTag.objects.create(**tag)

        # Add videos to database
        for video in VIDEOS:
            video = Video(**video)
            video.save()
            video.tags.add(VideoTag.objects.get(pk=random.randint(1, len(TAGS))))

    def setUp(self):
        """Setup client and request response"""
        self.client = Client()
        self.response = self.client.get("/videos")

    def test_videos_status(self):
        """Videos page returns 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        """Video page uses layout.html and videos.html"""
        self.assertTemplateUsed(
            self.response, "homepage/layout.html", "homepage/video.html"
        )

    def test_active_link(self):
        """Video page link is listed as active in navbar"""
        self.assertContains(
            self.response,
            '<a class="nav-link active" aria-current="page" href="/videos">Videos</a>',
        )

    def test_listed_all_video_titles(self):
        """All video titles found on videos page"""
        for video in VIDEOS:
            self.assertContains(self.response, f"{video['title']}")

    def test_listed_all_video_links(self):
        """All video links found on videos page"""
        for video in VIDEOS:
            self.assertContains(self.response, f"{video['source']}")

    def test_videos_in_sorted_order(self):
        """Videos are sorted by popularity"""
        videos = self.response.context["videos"]
        sorted_videos = sorted(VIDEOS, key=lambda video: video["views"], reverse=True)
        for i, video in enumerate(videos):
            self.assertEquals(video.title, sorted_videos[i]["title"])
