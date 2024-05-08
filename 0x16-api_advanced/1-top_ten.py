#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    resp = requests.get(url, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])

    else:
        print(None) 
