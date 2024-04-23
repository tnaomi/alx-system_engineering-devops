#!/usr/bin/python3
""" Call the JSONPlaceholder API, export data as JSON"""

import json
import requests as RQ
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = RQ.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(user_id)
            )

    name = user.json().get('username')
    todos = RQ.get('https://jsonplaceholder.typicode.com/todos')

    todo_dict = {}
    task_list = []

    for task in todos.json():
        if task.get('userId') == int(user_id):
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }
            task_list.append(task_dict)
        todo_dict[user_id] = task_list

    filename = user_id + '.json'

    with open(filename, mode="w") as f:
        json.dump(todo_dict, f)
