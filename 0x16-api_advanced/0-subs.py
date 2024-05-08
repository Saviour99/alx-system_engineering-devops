#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """A function to get the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'linux:0x16.api.advance:v1.0.0 (by /u/Sav_)'
    }

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False)
        resp.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = resp.json().get("data")
        return data.get("subscribers")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

