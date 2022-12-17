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

    def test_homepage_status(self):
        """Homepage returns 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_terms_sorted(self):
        response = self.client.get("/")
        history = response.context["history"]
        sorted_terms = sorted(TERMS, key=lambda term: (-term["year"], term["semester"]))
        for i, term in enumerate(history.keys()):
            self.assertEquals(sorted_terms[i]["semester"], term.semester)
            self.assertEquals(sorted_terms[i]["year"], term.year)
