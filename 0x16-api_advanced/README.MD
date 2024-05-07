# 0x16-api_advanced

## Authors

Tadala N. Kapengule

## Objectives

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Tasks

### 0. How many subs?

Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

*Hint*: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

*Requirements*:

-  *Prototype*: ``def number_of_subscribers(subreddit)``
-  If not a valid subreddit, return 0.
-  NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```python
python3 0-main.py programming
```

__File__

``0-subs.py``, test w ``0-main.py``

### 1. 