#!/usr/bin/python3
"""REDDIT API"""

import requests


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    resp = requests.get(url, allow_redirects=False)

    if resp.status_code != 200:
        return 0

    data = resp.json().get("data")
    return data.get("subscribers")
