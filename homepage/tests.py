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


class HomepageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        random.shuffle(TERMS)
        for term in TERMS:
            Term.objects.create(semester=term["semester"], year=term["year"])

        self.response = self.client.get("/")

    def test_homepage_status(self):
        """Homepage returns 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Homepage uses index.html and layout.html from homepage app"""
        self.assertTemplateUsed(self.response, "homepage/index.html")
        self.assertTemplateUsed(self.response, "homepage/layout.html")

    def test_name_included(self):
        """Name is included in homepage twice: once in meta title, once in title text"""
        self.assertContains(self.response, "Carter Zenke", count=2)

    def test_all_terms_listed_once(self):
        """All terms appear exactly once in HTML"""
        for term in TERMS:
            self.assertContains(
                self.response, f"{term['semester']} {term['year']}", count=1
            )

    def test_terms_sorted(self):
        """Terms are listed most to least recent"""
        history = self.response.context["history"]
        sorted_terms = sorted(TERMS, key=lambda term: (-term["year"], term["semester"]))
        for i, term in enumerate(history.keys()):
            self.assertEquals(sorted_terms[i]["semester"], term.semester)
            self.assertEquals(sorted_terms[i]["year"], term.year)
