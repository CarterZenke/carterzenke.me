from django.test import Client
from django.test import TransactionTestCase
from homepage.models import Course, Term, Video, VideoTag
import random


class VideoModelTestCase(TransactionTestCase):
    def setUp(self):
        pass

