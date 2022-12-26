from django.test import Client
from django.test import TestCase
from homepage.models import Course, Term
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
        pass

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
        pass

    def test_listed_all_video_links(self):
        """All video links found on videos page"""
        pass

    def test_videos_in_sorted_order(self):
        """Videos are sorted by recency"""
        pass
