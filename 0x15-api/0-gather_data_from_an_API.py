#!/usr/bin/python3
""" A Script that calls the JSONPlaceholder API"""


import requests as RQ
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    user = "{}/users/{}".format(url, sys.argv[1])
    response = RQ.get(user)
    json_data = response.json()
    print("Employee {} is done with tasks".format(json_data.get('name')),
          end="")

    todo = "{}/todos?userId={}".format(url, sys.argv[1])
    response = RQ.get(todo)
    tasks = response.json()
    task_list = []
    for el in tasks:
        if el.get("completed") is True:
            task_list.append(el)

    print("({}/{}):".format(len(task_list), len(tasks)))
    for el in task_list:
        print("\t {}".format(tasks.get("title")))
