from django.test import TestCase
from PIL.JpegImagePlugin import JpegImageFile
from homepage.helpers import get_yt_thumbnail


class GetThumbnailTestCase(TestCase):
    def test_valid_url_return_type(self):
        self.assertIs(type(get_yt_thumbnail("5aCAQyH-sko")), JpegImageFile)
        self.assertIs(type(get_yt_thumbnail("djmUUa6srSY")), JpegImageFile)
        self.assertIs(type(get_yt_thumbnail("5aCAQyH-sko")), JpegImageFile)
    
    def test_invalid_url_return_type(self):
        self.assertIs(type(get_yt_thumbnail("aaaaaaaaaaaaaaaaaa")), JpegImageFile)
        self.assertIs(type(get_yt_thumbnail("50")), JpegImageFile)
        self.assertIs(type(get_yt_thumbnail("à")), JpegImageFile)
