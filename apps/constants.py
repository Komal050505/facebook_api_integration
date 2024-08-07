"""
Constants Module

This module contains all the constants used in the Facebook API .

Constants:
    ACCESS_TOKEN (str): Facebook Page access token.
    PAGE_ID (str): Facebook Page ID.
    IMAGE_URL (str): URL of the image to be posted.
    CAPTION (str): Caption for the image.
    API_VERSION (str): Facebook Graph API version.
    LOG_SWITCH (bool): Toggle for enabling/disabling logging.
    FACEBOOK_GRAPH_URL (str): Base URL for Facebook Graph API.
    HEADERS (dict): Headers for HTTP requests.
    GIT_MSG (str): Message for GitHub link post.
    REPO_LINK (str): URL of the GitHub repository.
    GRAPH_API (str): Base URL for Facebook Graph API.
    POST_URI (str): URI for creating a post.
    PAYLOAD (dict): Payload template for creating a Facebook post.
"""

ACCESS_TOKEN = 'EAAVJnhaGsZCYBOzDZAj5xaCMuBda54JAVOYC4qUhXxd85mFAIHWN3G7Hyr6RG9Ura4JS6kM32NbExJIFrq4eYZCd5xkcuckS91x3UfnXlnIYkBUkcrtUyu6Fn6MlCb4pfYZCHWMQS5Uuf21VDPq0uOent3gfnYSy5v3JZCNPZBJwfkyD7DSXy678ZAl0eJQKfOJVYZBZBndVF'
PAGE_ID = '403714366157679'
IMAGE_URL = 'https://photos.app.goo.gl/eiXzJnqb8sj6Z4mVA'
CAPTION = 'KALKI Movie Poster'
API_VERSION = 'v12.0'
LOG_SWITCH = True
FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/'
HEADERS = {'Content-Type': 'application/json'}
GIT_MSG = "Github link of profile management repository"
REPO_LINK = "https://github.com/Komal050505/profile_managment_system"
GRAPH_API = "https://graph.facebook.com/"
POST_URI = "/feed?access_token="
PAYLOAD = {"message": None, "link": None, "published": False}
