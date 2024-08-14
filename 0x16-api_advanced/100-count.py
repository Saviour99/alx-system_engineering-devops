#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import re
import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            title = post['data']['title'].lower()
            hot_list.extend(re.findall(r'\w+', title))

        if after is not None:
            hot_list = count_words(subreddit, word_list, hot_list, after)

        word_counts = Counter(hot_list)
        sorted_counts = sorted([(word, word_counts[word])
                               for word in word_list if word_counts[word] > 0],
                               key=lambda x: (-x[1], x[0].lower()))

        for word, count in sorted_counts:
            print(f"{word}: {count}")

    else:
        return
