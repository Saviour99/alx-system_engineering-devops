#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """
    Recursive function that queries the Reddit API,
    parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()

        # Normalize word_list to lowercase
        word_list = [word.lower() for word in word_list]

        # Process titles in the current page of results
        for post in data['data']['children']:
            title = post['data']['title'].lower().split()
            for word in title:
                if word in word_list:
                    word_count[word] = word_count.get(word, 0) + 1

        # Check if there are more pages to process (pagination)
        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            # Sort and print results when recursion ends
            if word_count:
                sorted_word_count = sorted(word_count.items(),
                                           key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return
