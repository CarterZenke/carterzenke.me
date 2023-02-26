import os
import PIL
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
import requests
from requests import HTTPError


def get_yt_video_statistics(id: str) -> dict:
    """Queries YouTube API for public statistics associated with video ID"""

    # Get API key from environment
    API_KEY = os.environ["YT_API_KEY"]

    # Make request
    response = requests.get(
        f"https://youtube.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={API_KEY}"
    )
    response.raise_for_status()

    # Return statistics if videos returned
    return response.json()["items"][0]["statistics"]


def get_yt_thumbnail(id: str) -> JpegImageFile:
    """Returns PIL JpegImageFile object of thumbnail from YT video ID"""
    URL = f"https://img.youtube.com/vi/{id}/hqdefault.jpg"
    
    with requests.get(URL, stream=True) as response:

        # URL always returns JPEG, whether valid ID or not
        return Image.open(response.raw)