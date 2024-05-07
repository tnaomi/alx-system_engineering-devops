#!/usr/bin/python3

""" Query the Reddit API for subreddit subscribers"""


def top_ten(subreddit):
    """ Query a Reddit subreddit for the total number of subscribers.
    Avoid redirects to search results if invalid subreddit.
    @Param: subreddit
    Returns: 0 if not valid subreddit
    """
    import requests as RQ

    SUB_URL = 'http://reddit.com/r/{}/hot/.json?limit=10'.format((subreddit))

    agent = {'user-agent': 'my-api/0.0.1'}

    resp = RQ.get(SUB_URL, headers=agent, allow_redirects=False)

    if (resp.status_code != 200):
        print(None)
        return None

    try:
        json_resp = resp.json()

    except ValueError:
        print(None)
        return None

    try:
        data = json_resp.get('data')
        child = json_resp.get('children')

        for entry in child[:10]:
            hot_post = entry.get('data')
            print(hot_post.get('title'))

    except:
        return None
