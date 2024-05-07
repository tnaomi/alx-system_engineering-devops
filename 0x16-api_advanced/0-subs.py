#!/usr/bin/python3

""" Query the Reddit API for subreddit subscribers"""

import requests as RQ

def number_of_subscribers(subreddit):
    """ Query a Reddit subreddit for the total number of subscribers.
    Avoid redirects to search results if invalid subreddit.
    @Param: subreddit
    Returns: 0 if not valid subreddit
    """
    SUB_URL = 'http://reddit.com/r/{}/about.json'.format(str(subreddit))

    agent = {'user-agent': 'my-api/0.0.1'}

    resp = RQ.get(SUB_URL, headers=agent, allow_redirects=False)

    if (resp.status_code != 200):
        return 0

    try:
        json_resp = resp.json()

    except:
        return 0
    
    data = json_resp.get('data')

    if data:
        subs = data.get('subscribers')
        if subs:
            return subs

    return 0