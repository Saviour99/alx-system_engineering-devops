#!/usr/bin/python3
"""REDDIT API"""

import requests


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API"""
    urlEndPoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        resp = requests.get(urlEndPoint,
                            headers=headers,
                            allow_redirects=False)

        if resp.status_code != 200:
            return 0

        data = resp.json().get("data")
        return data.get("subscribers")
    except requests.RequestException:
        return 0
