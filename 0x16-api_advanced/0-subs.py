#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """A function to get the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    resp = requests.get(url, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        subscribers = data.get("data")
        return subscribers.get("subscribers")
    else:
        return 0
