#!/usr/bin/python3
""" A Script that calls the JSONPlaceholder API"""


import requests as RQ
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    employee = '{}users/{}'.format(url, user_id)
    response = RQ.get(employee)
    json_data = response.json()
    print("Employee {} is done with tasks".format(json_data.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, user_id)
    response = RQ.get(todos)
    tasks = response.json()
    task_list = []
    for task in tasks:
        if task.get('completed') is True:
            task_list.append(task)

    print("({}/{}):".format(len(task_list), len(tasks)))
    for task in task_list:
        print("\t {}".format(task.get("title")))
