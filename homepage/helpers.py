import os
import requests
from requests import HTTPError


def get_yt_video_statistics(id: str) -> dict:
    """Queries YouTube API for public statistics associated with video ID"""
    
    # Get API key from environment
    API_KEY = os.environ['YT_API_KEY']

    # Make request
    try:
        response = requests.get(f"https://youtube.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={API_KEY}")
        response.raise_for_status()
    except HTTPError:
        return None
    
    # Return statistics if videos returned
    try:
        return response.json()["items"][0]["statistics"]
    except IndexError:
        return None