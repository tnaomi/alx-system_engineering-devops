#!/usr/bin/python3

""" Query the Reddit API for hot topics"""


def count_words(subreddit, word_list, after='', words={}):
    """ Query a Reddit subreddit for the list of hot topics.
    Avoid redirects to search results if invalid subreddit.
    @Param1: subreddit,
    @Param2: word list,
    @Param3: after,
    @Param4: words.
    Returns: 0 if not valid subreddit
    """
    import requests as RQ

    if not words:
        for word in word_list:
            words[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for single in word_list:
            if single[1]:
                print("{}: {}".format(single[0].lower(), single[1]))
        return None

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
            hot_post_title = hot_post.get('title')
            lower = [s.lower() for s in title.split(' ')]

            for single in word_list:
                word_dic[single] += lower.count(single.lower())

    except:
        return None

    count_words(subreddit, word_list, after, words)
