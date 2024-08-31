#!/usr/bin/python3
import requests

"""
number_of_subscribers - queries the reddit api
returns: the number of subscribers of given subreddit
"""

def number_of_subscribers(subreddit):
    """
    queries to reddit api
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
            'User-Agent': 'Chrome/128.0.6613.114 by Sad_Dig_6145'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"response JSON: {data}")

            subscribers = data['data'].get('subscribers', 0)
            print(f"Number of subscribers: {subscribers}")
            return subscribers
        elif response.status_code == 302:
            print("Redirect detected - Subredit may not exist.")
            return 0
        else:
            print(f"Unexpected status code: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Request failed:{e}")
        return 0

