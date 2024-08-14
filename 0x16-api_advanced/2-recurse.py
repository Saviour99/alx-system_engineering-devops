#!/usr/bin/python3
"""
A recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddi
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    resp = requests.get(url, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        if after:
            hot_list = recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
