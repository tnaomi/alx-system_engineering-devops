#!/usr/bin/python3

""" Query the Reddit API for hot topics"""


def recurse(subreddit, hot_list=[], after=''):
    """ Query a Reddit subreddit for the list of hot topics.
    Avoid redirects to search results if invalid subreddit.
    @Param1: subreddit,
    @Param2: hot list,
    @Param3: after.
    Returns: 0 if not valid subreddit
    """
    import requests as RQ

    if after is None:
        return hot_list

    SUB_URL = 'http://reddit.com/r/{}/hot/.json'.format((subreddit))

    agent = {'user-agent': 'my-api/0.0.1'}

    parameters = {
        'limit': 100,
        'after': after
    }

    resp = RQ.get(SUB_URL, headers=agent, params=parameters,
                  allow_redirects=False)

    if (resp.status_code != 200):
        return None

    try:
        json_resp = resp.json()

    except ValueError:
        return None

    try:
        data = json_resp.get('data')
        child = json_resp.get('children')
        after = data.get('after')

        for entry in child[:10]:
            hot_post = entry.get('data')
            hot_list.append(hot_post.get('title'))

    except:
        return None

    return recurse(subreddit, hot_list, after)
